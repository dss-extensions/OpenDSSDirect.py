# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

from . import dss, DSSException

# Author: Michael Blonsky, michael.blonsky@nrel.gov

ELEMENT_CLASSES = {
    'Load': dss.Loads,
    'PV': dss.PVsystems,
    'Generator': dss.Generators,
    'Line': dss.Lines,
    'Xfmr': dss.Transformers,
}
LINE_CLASSES = ['Line', 'Xfmr']


class Wrapper:
    def __init__(self, redirects, time_step, start_time):
        self.dss = dss

        # Run redirect files before main dss file
        print('DSS Compiling...')
        if not isinstance(redirects, list):
            redirects = [redirects]
        for redirect in redirects:
            self.redirect(redirect)

        # check if elements exist. If storage exists, save storage names
        self.included_elements = [class_name for class_name in ['Load', 'PV', 'Generator']
                                  if len(ELEMENT_CLASSES[class_name].AllNames()) > 0]
        storages = self.get_all_elements('Storage')
        if len(storages):
            self.included_elements.append('Storage')
            self.storage_names = storages.index.str.replace('Storage.', '').to_list()
        else:
            self.storage_names = []

        # Set to QSTS Mode
        self.run_command('set mode=yearly')
        # dss.Solution.Mode(2)  # should set mode to yearly

        dss.Solution.Number(1)  # Number of Monte Carlo simulations
        day_of_year = start_time.timetuple().tm_yday - 1
        dss.Solution.Hour(day_of_year * 24 + start_time.hour)  # QSTS starting hour of year

        # Run, without advancing, then set step size
        dss.Solution.StepSize(0)
        self.run_dss()
        dss.Solution.StepSize(time_step.total_seconds())

        print('DSS Compiled Circuit:', dss.Circuit.Name())

    @staticmethod
    def run_command(cmd):
        status = dss.run_command(cmd)
        if status:
            print('DSS Status ({}): {}'.format(cmd, status))

    def redirect(self, filename):
        print('DSS Running file:', filename)
        self.run_command('Redirect ' + filename)

    def run_dss(self, no_controls=False):
        try:
            if no_controls:
                status = dss.Solution.SolveNoControl()
            else:
                status = dss.Solution.Solve()
            if status:
                print('DSS Solve Status: {}'.format(status))

            if 'Storage' in self.included_elements:
                dss.Circuit.UpdateStorage()

        except Exception as e:
            self.run_command('export Eventlog')
            raise e

    # GENERAL GET METHODS

    @staticmethod
    def get_all_buses():
        return dss.Circuit.AllBusNames()

    @staticmethod
    def get_all_elements(element='Load'):
        if element in ELEMENT_CLASSES:
            cls = ELEMENT_CLASSES[element]
            df = dss.utils.to_dataframe(cls)
        else:
            df = dss.utils.class_to_dataframe(element, transform_string=lambda x: pd.to_numeric(x, errors='ignore'))
            # df = dss.utils.class_to_dataframe(element)
        return df

    @staticmethod
    def get_circuit_power():
        # returns negative of circuit power (positive = consuming power)
        powers = dss.Circuit.TotalPower()
        if len(powers) == 2:
            p, q = tuple(powers)
            p, q = -p, -q
        elif len(powers) == 6:
            p = powers[0:2:]
            q = powers[1:2:]
        else:
            raise DSSException('Expected 1- or 3-phase circuit')
        if np.isnan(p) or np.isnan(q):
            raise DSSException('NaN output for circuit power: ({}, {})'.format(p, q))
        return p, q

    @staticmethod
    def get_losses():
        p, q = dss.Circuit.Losses()
        return p / 1000, q / 1000

    def get_total_power(self, element='Load'):
        p_total, q_total = 0, 0

        if element in ELEMENT_CLASSES:
            cls = ELEMENT_CLASSES[element]
            all_names = cls.AllNames()
            for name in all_names:
                p, q = self.get_power(name, element, total=True)
                p_total += p
                q_total += q
        elif element == 'Storage' and 'Storage' in self.included_elements:
            # reversing sign for storage
            storage_p = [-self.get_property(name, 'kW', 'Storage') for name in self.storage_names]
            storage_q = [-self.get_property(name, 'kvar', 'Storage') for name in self.storage_names]
            p_total = sum(storage_p)
            q_total = sum(storage_q)

        return p_total, q_total

    def get_circuit_info(self):
        # TODO: Add powers by phase if 3-phase; options to add/remove element classes
        p_total, q_total = self.get_circuit_power()
        p_loss, q_loss = self.get_losses()
        total_by_class = {class_name: self.get_total_power(class_name) for class_name in self.included_elements}

        out = {'Total P (MW)': p_total / 1000,
               'Total Loss P (MW)': p_loss / 1000,
               }
        for class_name, (p, q) in total_by_class.items():
            out['Total {} P (MW)'.format(class_name)] = p / 1000

        out.update({'Total Q (MVAR)': q_total / 1000,
                    'Total Loss Q (MVAR)': q_loss / 1000,
                    })
        for class_name, (p, q) in total_by_class.items():
            out['Total {} Q (MVAR)'.format(class_name)] = q / 1000

        return out

    # VOLTAGE METHODS

    @staticmethod
    def get_bus_voltage(bus, phase=None, pu=True, polar=True, mag_only=True, average=False):
        dss.Circuit.SetActiveBus(bus)

        if polar:
            if pu:
                v = dss.Bus.puVmagAngle()
            else:
                v = dss.Bus.VMagAngle()
            if any([x <= 0 for x in v[::2]]):
                raise DSSException('Bus "{}" voltage = {}, out of bounds'.format(bus, v))
        else:
            if pu:
                v = dss.Bus.PuVoltage()
            else:
                v = dss.Bus.Voltages()

        # if phase selected, only keep voltages from given phase
        if phase is None:
            pass
        elif phase - 1 in range(len(v) // 2):
            v = v[2 * (phase - 1): 2 * phase]
        else:
            raise DSSException('Bad phase for Bus {}: {}'.format(bus, phase))

        # Remove angles if voltages in polar coordinates
        if polar and mag_only:
            v = v[::2]

        # return a float if only returning 1 voltage, otherwise return a tuple
        if any([np.isnan(x) for x in v]):
            raise DSSException('NaN output for bus voltage: {}'.format(bus))

        if len(v) == 1:
            return v[0]
        else:
            if average:
                return sum(v) / len(v)
            else:
                return tuple(v)

    @staticmethod
    def set_element(name, element):
        # same as: dss.Circuit.SetActiveElement(self.__Class + '.' + self.__Name)
        name = name.lower()
        if element in ELEMENT_CLASSES:
            cls = ELEMENT_CLASSES[element]
        else:
            dss.Circuit.SetActiveClass(element)
            cls = dss.ActiveClass
        cls.Name(name)

        if cls.Name() != name:
            raise DSSException('{} "{}" does not exist'.format(element, name))

    def get_voltage(self, name, element='Load', **kwargs):
        # note: for lines/transformers, always takes voltage from Bus1
        self.set_element(name, element)
        bus = dss.CktElement.BusNames()[0]
        if dss.CktElement.NumPhases() == 1:
            kwargs['phase'] = 1
        return self.get_bus_voltage(bus, **kwargs)

    def get_all_bus_voltages(self, **kwargs):
        # gets all bus voltages, by phase
        buses = self.get_all_buses()

        data = {}
        for bus in buses:
            v = self.get_bus_voltage(bus, **kwargs)
            if isinstance(v, tuple):
                data.update({bus + '.' + str(i + 1): v_ph for i, v_ph in enumerate(v)})
            else:
                data[bus] = v
        return data

    # POWER METHODS

    def get_power(self, name, element='Load', phase=None, total=False, line_bus=1, raw=False):
        # Returns the current power of the element/line (note line used for lines and xfmrs)
        #  - If raw==True: returns raw data from dss.CktElement.Powers(), as tuple
        #  - If 1-ph element: returns (P, Q) tuple
        #  - If 3-ph element: returns ((Pa, Pb, Pc), (Qa, Qb, Qc)) tuple, or (P, Q) if phase is specified or total==True
        #  - If 1-ph line: returns (P, Q) tuple of first bus (second bus if line_bus==2)
        #  - If 3-ph line: returns ((Pa, Pb, Pc), (Qa, Qb, Qc)) tuple, or (P, Q) if phase is specified or total==True
        # Note: Returns power with the sign convention: positive=consuming
        self.set_element(name, element)
        powers = dss.CktElement.Powers()

        if raw:
            return tuple(powers)

        n_phases = dss.CktElement.NumPhases()
        if element in LINE_CLASSES:
            # remove zeros and second bus
            start = (line_bus - 1) * len(powers) // 2
            powers = powers[start: start + 2 * n_phases]
        else:
            # remove 2 trailing zeros
            powers = powers[:-2]

        if n_phases == 1:
            return tuple(powers)
        elif n_phases in [2, 3]:
            if phase is None:
                p = tuple(powers[0:2 * n_phases:2])
                q = tuple(powers[1:2 * n_phases + 1:2])
                if total:
                    return sum(p), sum(q)
                else:
                    return p, q
            if phase - 1 in range(n_phases):
                powers = powers[(phase - 1) * 2: phase * 2]
                return tuple(powers)
        else:
            raise DSSException('Bad phase for {} {}: {}'.format(element, name, phase))

    def set_power(self, name, p=None, q=None, element='Load', size=None):
        if element in ELEMENT_CLASSES:
            self.set_element(name, element)
            cls = ELEMENT_CLASSES[element]
            if p is not None:
                cls.kW(p)
            if q is not None:
                cls.kvar(q)
        elif element == 'Storage':
            if p == 0:
                self.run_command('edit {}.{} kW=0 kvar=0 State=Idling'.format(element, name))
                return

            if size is None:
                size = self.get_property(name, 'kWrated', element='Storage')
            if q is None:
                q = 0
            # calculate power factor and percent charge/discharge
            pf = np.cos(np.arctan(q / p))
            if p * q < 0:
                pf = -pf  # negative PF when P and Q are opposite sign
            p_pct = abs(p) / size * 100

            if p < 0:
                self.run_command(
                    'edit {}.{} %discharge={:.4} pf={:.4} State=Discharging'.format(element, name, p_pct, pf))
            else:
                self.run_command('edit {}.{} %charge={:.4} pf={:.4} State=Charging'.format(element, name, p_pct, pf))
        else:
            raise DSSException("Unknown element class:", element)

    def get_all_complex(self, name, element='Load'):
        self.set_element(name, element)
        return {
            'Voltages': dss.CktElement.Voltages(),
            'VoltagesMagAng': dss.CktElement.VoltagesMagAng(),
            'Currents': dss.CktElement.Currents(),
            'CurrentsMagAng': dss.CktElement.CurrentsMagAng(),
            'Powers': dss.CktElement.Powers(),
        }

    # PROPERTY METHODS

    def get_property(self, name, property_name, element='Load'):
        self.set_element(name, element)
        all_properties = dss.Element.AllPropertyNames()
        if property_name not in all_properties:
            raise DSSException('Could not find {} property for {} "{}"'.format(property_name, element, name))

        idx = all_properties.index(property_name)
        value = dss.Properties.Value(str(idx + 1))

        try:
            number = float(value)
            return number
        except ValueError:
            return value

    def set_property(self, name, property_name, value, element='Load'):
        self.set_element(name, element)
        all_properties = dss.Element.AllPropertyNames()
        if property_name not in all_properties:
            raise DSSException('Could not find {} property for {} "{}"'.format(property_name, element, name))

        idx = all_properties.index(property_name)
        dss.Properties.Value(str(idx + 1), str(value))

        new_value = self.get_property(name, property_name, element)
        assert new_value == value

    @staticmethod
    def set_tap(name, tap, max_tap=16):
        dss.RegControls.Name(name)
        tap = min(max(int(tap), -max_tap), max_tap)
        dss.RegControls.TapNumber(tap)

    @staticmethod
    def get_tap(name):
        dss.RegControls.Name(name)
        return int(dss.RegControls.TapNumber())
