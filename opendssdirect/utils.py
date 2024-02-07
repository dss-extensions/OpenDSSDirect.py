import inspect
import warnings
from dss_python_backend import enums
from .Bases import Iterable

is_pandas_installed = True

try:
    import pandas as pd
except ImportError:
    is_pandas_installed = False


class Iterator:
    def __init__(self, module, function):
        warnings.warn("OpenDSSDirect.py's Iterator is deprecated; you can use native Python iterators directly now.", DeprecationWarning, stacklevel=2)
        assert inspect.ismodule(module) or isinstance(module, Iterable), "{module} must be of type module or a DSS iterable".format(
            module=module
        )
        self.module = module
        self.function = function

    def __iter__(self):
        from opendssdirect import dss

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
    """
    Use the Text interface of OpenDSS, grabbing all output text in a string.
    
    This is **deprecated** since it doesn't handle errors as exceptions and can confuse users.

    Prefer using [`dss("commands")`](#opendssdirect.OpenDSSDirect.OpenDSSDirect.__call__), [`dss.Text.Command("command")`](#opendssdirect.Text.IText.Command), or [`dss.Text.Commands("commands")`](#opendssdirect.Text.IText.Commands),.
    """

    warnings.warn('run_command is deprecated (use Command, Commands or the callable shortcut), see https://github.com/dss-extensions/OpenDSSDirect.py/issues/70', 
                  DeprecationWarning, stacklevel=2)

    if dss is None:
        from opendssdirect import dss

    api_util = dss.Basic._api_util
    r = []
    for l in text.splitlines():
        dss.dss_lib.Text_Set_Command(l.encode(api_util.codec))
        r.append(api_util.get_string(dss.dss_lib.Text_Get_Result()))

    return "\n".join(r).strip()


def to_dataframe(module):
    """
    Iterate and export all data from the classic API class/module to a dataframe.

    If Pandas is not available, a dict of dicts is returned.
    """
    data = dict()

    for e in module:
        data[e.Name()] = dict()

    if len(data) != 0:
        for element in module:
            element_name = element.Name()
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
            "Pandas was not installed. Please see documentation for how to install extra dependencies."
        )
        return data


def _clean_data(data, class_name):
    from opendssdirect import dss

    for element in dss.ActiveClass.AllNames():
        name = "{class_name}.{element}".format(class_name=class_name, element=element)
        dss.ActiveClass.Name(element)

        all_prop_names = dss.Element.AllPropertyNames()
        if "NConds" in all_prop_names:
            nconds = int(data[name]["NConds"])
            x = []
            h = []
            units = []

            for cond in range(1, nconds + 1):
                dss("{name}.cond={cond}".format(name=name, cond=cond))

                dss("? {name}.x".format(name=name))
                x.append(float(dss.Text.Result()))

                dss("? {name}.h".format(name=name))
                h.append(float(dss.Text.Result()))

                dss("? {name}.units".format(name=name))
                units.append(dss.Text.Result())

            data[name]["X"] = x
            data[name]["H"] = h
            data[name]["Units"] = units

        elif "nconds" in all_prop_names: # backwards compat
            nconds = int(data[name]["nconds"])
            x = []
            h = []
            units = []

            for cond in range(1, nconds + 1):
                dss("{name}.cond={cond}".format(name=name, cond=cond))

                dss("? {name}.x".format(name=name))
                x.append(float(dss.Text.Result()))

                dss("? {name}.h".format(name=name))
                h.append(float(dss.Text.Result()))

                dss("? {name}.units".format(name=name))
                units.append(dss.Text.Result())

            data[name]["x"] = x
            data[name]["h"] = h
            data[name]["units"] = units

    return data


def class_to_dataframe(class_name, dss=None, transform_string=None, clean_data=None):
    """
    Export all DSS properties for a selected DSS object class.

    This function uses the `ActiveClass`, `Element` and `Properties` interfaces to iterate through the elements, extracting the value of each DSS property.

    Caveats are:

    - All properties are exported; this can be misleading since the order of definition and which properties are used can change how the DSS models behave.
    - All data is exported as text and must be reinterpreted in Python.
    - It can be slow for large circuits.

    Due to these caveats, the function has been marked **deprecated**. Still, it has been used by many third-party software as a way to extract important data, so it will be kept for backwards compatibility.

    For alternatives:
    
    - Check the functions for JSON output, such as [`Circuit.ToJSON()`](#opendssdirect.Circuit.ICircuit.ToJSON) (whole circuit), [`ActiveClass.ToJSON()`](#opendssdirect.ActiveClass.IActiveClass.ToJSON) (a whole class), and [`Element.ToJSON()`](#opendssdirect.Element.IElement.ToJSON). The DSS-Python examples are a good starting point (all related functions are also available in OpenDSSDirect.py): https://dss-extensions.org/dss_python/examples/JSON/
    - The JSON output/input, and other future alternatives are based on the work-in-progress AltDSS Schema project. Check https://github.com/dss-extensions/AltDSS-Schema
    
    """
    warnings.warn("class_to_dataframe is deprecated; it will not be removed any time soon, using JSON exports is preferable. Watch AltDSS-Python for future alternatives, including native dataframes.", DeprecationWarning, stacklevel=2)

    if transform_string is None:
        transform_string = _evaluate_expression

    if clean_data is None:
        clean_data = _clean_data

    if not callable(transform_string):
        raise TypeError(
            "The `transform_string` must be a callable. Please check the documentation or contact the developer."
        )

    if dss is None:
        from opendssdirect import dss

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
        from opendssdirect import dss
    return to_dataframe(dss.Capacitors)


def fuses_to_dataframe(dss=None):
    if dss is None:
        from opendssdirect import dss
    return to_dataframe(dss.Fuses)


def generators_to_dataframe(dss=None):
    if dss is None:
        from opendssdirect import dss
    return to_dataframe(dss.Generators)


def isource_to_dataframe(dss=None):
    if dss is None:
        from opendssdirect import dss
    return to_dataframe(dss.Isource)


def lines_to_dataframe(dss=None):
    if dss is None:
        from opendssdirect import dss
    return to_dataframe(dss.Lines)


def loadshape_to_dataframe(dss=None):
    if dss is None:
        from opendssdirect import dss
    return to_dataframe(dss.LoadShape)


def loads_to_dataframe(dss=None):
    if dss is None:
        from opendssdirect import dss
    return to_dataframe(dss.Loads)


def meters_to_dataframe(dss=None):
    if dss is None:
        from opendssdirect import dss
    return to_dataframe(dss.Meters)


def monitor_to_dataframe(dss=None):
    """
    Return the data from current active monitor as a Pandas DataFrame
    """
    if dss is None:
        from opendssdirect import dss

    if dss.Solution.Mode() in (enums.SolveModes.Harmonic, enums.SolveModes.HarmonicT):
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
        from opendssdirect import dss
    return to_dataframe(dss.Monitors)


def pvsystems_to_dataframe(dss=None):
    if dss is None:
        from opendssdirect import dss
    return to_dataframe(dss.PVsystems)


def regcontrols_to_dataframe(dss=None):
    if dss is None:
        from opendssdirect import dss
    return to_dataframe(dss.RegControls)


def reclosers_to_dataframe(dss=None):
    if dss is None:
        from opendssdirect import dss
    return to_dataframe(dss.Reclosers)


def relays_to_dataframe(dss=None):
    if dss is None:
        from opendssdirect import dss
    return to_dataframe(dss.Relays)


def sensors_to_dataframe(dss=None):
    if dss is None:
        from opendssdirect import dss
    return to_dataframe(dss.Sensors)


def transformers_to_dataframe(dss=None):
    if dss is None:
        from opendssdirect import dss
    return to_dataframe(dss.Transformers)


def vsources_to_dataframe(dss=None):
    if dss is None:
        from opendssdirect import dss
    return to_dataframe(dss.Vsources)


def xycurves_to_dataframe(dss=None):
    if dss is None:
        from opendssdirect import dss
    return to_dataframe(dss.XYCurves)
