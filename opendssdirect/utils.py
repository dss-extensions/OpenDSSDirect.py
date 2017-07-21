import inspect
import pandas as pd
import warnings


class Iterator(object):
    def __init__(self, module, function):
        assert inspect.ismodule(module), '{module} must be of type module'.format(module=module)
        self.module = module
        self.function = function

    def __iter__(self):
        self.module.First()

        while True:

            yield getattr(self.module, self.function)

            if not self.module.Next() > 0:
                break


def run_command(text, dss=None):
    '''Use Text interface of OpenDSS'''
    if dss is None:
        from . import dss

    return dss.dss_lib.DSSPut_Command(text.encode('ascii')).decode('ascii')


def to_dataframe(module):
    data = dict()

    for e in module.AllNames():
        data[e] = dict()

    if len(data) != 0:

        for i in Iterator(module, 'Name'):
            element_name = i()
            data[element_name] = {n: getattr(module, n)() for n, f in getmembers(module)}
    else:
        class_name = module.__name__
        warnings.warn("Empty element type ({class_name})".format(class_name=class_name))

    return pd.DataFrame(data).T


def getmembers(module):

    for n, f in inspect.getmembers(module):

        if n != 'AllNames' and n != 'Next' and n != 'First' and not (n.startswith('__') and n.endswith('__')):
            yield n, f


def capacitors_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.Capacitors)


def fuses_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.Fuses)


def generators_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.Generators)


def isource_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.Isource)


def lines_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.Lines)


def loadshape_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.LoadShape)


def loads_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.Loads)


def meters_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.Meters)


def monitors_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.Monitors)


def pvsystems_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.PVsystems)


def regcontrols_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.RegControls)


def reclosers_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.Reclosers)


def relays_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.Relays)


def sensors_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.Sensors)


def transformers_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.Transformers)


def vsources_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.Vsources)


def xycurves_to_dataframe(dss=None):
    if dss is None:
        import opendssdirect as dss
    return to_dataframe(dss.XYCurves)
