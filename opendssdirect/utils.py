import inspect
import warnings

from ._utils import get_string, dss_py
from . import _utils

is_pandas_installed = True

try:
    import pandas as pd
except ImportError:
    is_pandas_installed = False


class Iterator(object):
    def __init__(self, module, function):
        assert inspect.ismodule(module), "{module} must be of type module".format(
            module=module
        )
        self.module = module
        self.function = function

    def __iter__(self):
        import opendssdirect as dss

        try:
            idx = self.module.First()
        except:
            return # no circuit?

        if dss.Error.ExtendedErrors() and idx == 0:
                return # nothing to iterate

        while True:

            yield getattr(self.module, self.function)

            if not self.module.Next() > 0:
                break


def run_command(text, dss=None):
    """Use Text interface of OpenDSS"""
    if dss is None:
        import opendssdirect as dss

    r = []
    for l in text.splitlines():
        dss.dss_lib.Text_Set_Command(l.encode(_utils.codec))
        r.append(get_string(dss.dss_lib.Text_Get_Result()))

    return "\n".join(r).strip()


def to_dataframe(module):
    data = dict()

    for e in Iterator(module, "Name"):
        data[e()] = dict()

    if len(data) != 0:

        for i in Iterator(module, "Name"):
            element_name = i()
            data[element_name] = {
                n: getattr(module, n)() for n, f in getmembers(module)
            }
    else:
        class_name = module.__name__
        warnings.warn("Empty list ({class_name})".format(class_name=class_name))

    if is_pandas_installed:
        return pd.DataFrame(data).T
    else:
        warnings.warn(
            "Pandas cannot be installed. Please see documentation for how to install extra dependencies."
        )
        return data


def _clean_data(data, class_name):
    import opendssdirect as dss

    for element in dss.ActiveClass.AllNames():
        name = "{class_name}.{element}".format(class_name=class_name, element=element)
        dss.ActiveClass.Name(element)

        if "nconds" in dss.Element.AllPropertyNames():
            nconds = int(data[name]["nconds"])
            x = []
            h = []
            units = []

            for cond in range(1, nconds + 1):
                dss.run_command("{name}.cond={cond}".format(name=name, cond=cond))
                x.append(float(dss.run_command("? {name}.x".format(name=name))))
                h.append(float(dss.run_command("? {name}.h".format(name=name))))
                units.append(dss.run_command("? {name}.units".format(name=name)))

            data[name]["x"] = x
            data[name]["h"] = h
            data[name]["units"] = units

    return data


def class_to_dataframe(class_name, dss=None, transform_string=None, clean_data=None):

    if transform_string is None:
        transform_string = _evaluate_expression

    if clean_data is None:
        clean_data = _clean_data

    if not callable(transform_string):
        raise TypeError(
            "The `transform_string` must be a callable. Please check the documentation or contact the developer."
        )

    if dss is None:
        import opendssdirect as dss

    dss.Circuit.SetActiveClass("{class_name}".format(class_name=class_name))
    if class_name.lower() != dss.ActiveClass.ActiveClassName().lower():
        raise NotImplementedError(
            "`{class_name}` is not supported by the `class_to_dataframe` interface, please contact the developer for more information.".format(
                class_name=class_name
            )
        )
    data = dict()

    for element in dss.ActiveClass.AllNames():
        name = "{class_name}.{element}".format(class_name=class_name, element=element)
        dss.ActiveClass.Name(element)

        data[name] = dict()
        for i, n in enumerate(dss.Element.AllPropertyNames()):
            # use 1-based index for compatibility with previous versions
            string = dss.Properties.Value(str(i + 1))

            data[name][n] = transform_string(string)

    data = clean_data(data, class_name)

    if is_pandas_installed:
        return pd.DataFrame(data).T
    else:
        warnings.warn(
            "Pandas is not installed. Please see documentation for how to install extra dependencies."
        )
        return data


def _evaluate_expression(string):

    if "[" in string and "]" in string:
        e = [
            _evaluate_expression(x.strip())
            for x in string.replace("[", "").replace("]", "").split(",")
            if x.strip() != ""
        ]

        return e

    elif string.startswith("(") and string.endswith(")"):
        e = tuple(
            _evaluate_expression(x.strip())
            for x in string.replace("(", "").replace(")", "").split(",")
            if x.strip() != ""
        )
        return e

    elif string.lower() == "true":
        return True

    elif string.lower() == "false":
        return False

    else:
        return string


def getmembers(module):
    for n in module._columns:
        if n not in ("AllNames", "Next", "First"):
            yield n, getattr(module, n)


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


def monitor_to_dataframe(dss=None):
    """
    Return the data from current active monitor as a Pandas DataFrame
    """
    if dss is None:
        import opendssdirect as dss

    if dss.Solution.Mode() in (dss_py.enums.SolveModes.Harmonic, 17):
        # Note: Mode 17 is HarmonicT but it was not exposed in the enum
        #       ported from COM as of 2021-01-03
        columns = ['frequency', 'harmonic']
    else:
        columns = ['hour', 'second']

    columns.extend(col.strip() for col in dss.Monitors.Header())
    data = dss.Monitors.AsMatrix()

    if is_pandas_installed:
        return pd.DataFrame(data, columns=columns)
    else:
        warnings.warn(
            "Pandas is not installed. Please see documentation for how to install extra dependencies."
        )
        return dict(zip(columns, data.T))


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
