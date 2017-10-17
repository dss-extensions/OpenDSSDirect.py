import inspect
import warnings

is_pandas_installed = True

try:
    import pandas as pd
except ImportError:
    is_pandas_installed = False


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

    r = []
    for l in text.splitlines():
        r.append(dss.dss_lib.DSSPut_Command(l.encode('ascii')).decode('ascii'))

    return '\n'.join(r)


def to_dataframe(module):
    data = dict()

    for e in Iterator(module, 'Name'):
        data[e()] = dict()

    if len(data) != 0:

        for i in Iterator(module, 'Name'):
            element_name = i()
            data[element_name] = {n: getattr(module, n)() for n, f in getmembers(module)}
    else:
        class_name = module.__name__
        warnings.warn("Empty element type ({class_name})".format(class_name=class_name))

    if is_pandas_installed:
        return pd.DataFrame(data).T
    else:
        warnings.warn("Pandas cannot be installed. Please see documentation for how to install extra dependencies.")
        return data


def class_to_dataframe(class_name, dss=None):

    if dss is None:
        import opendssdirect as dss

    dss.Circuit.SetActiveClass(
        '{class_name}'.format(
            class_name=class_name
        )
    )
    if class_name.lower() != dss.ActiveClass.ActiveClassName().lower():
        raise NotImplementedError(
            "`{class_name}` is not supported by the `class_to_dataframe` interface, please contact the developer for more information.".format(
                class_name=class_name,
            )
        )
    data = dict()

    for element in dss.ActiveClass.AllNames():
        name = '{class_name}.{element}'.format(
            class_name=class_name,
            element=element
        )
        dss.Circuit.SetActiveElement(name)

        data[name] = dict()
        for i, n in enumerate(dss.CktElement.AllPropertyNames()):
            string = dss.Properties.Value(str(i + 1))

            data[name][n] = _evaluate_expression(string)

    if is_pandas_installed:
        return pd.DataFrame(data).T
    else:
        warnings.warn(
            "Pandas cannot be installed. Please see documentation for how to install extra dependencies."
        )
        return data


def _evaluate_expression(string):

    if '[' in string and ']' in string:
        e = [_evaluate_expression(x.strip()) for x in string.replace('[', '').replace(']', '').split(',') if x.strip() != '']

        return e

    elif '(' in string and ')' in string:
        e = tuple(_evaluate_expression(x.strip()) for x in string.replace('(', '').replace(')', '').split(',') if x.strip() != '')
        return e

    elif string.lower() == 'true':
        return True

    elif string.lower() == 'false':
        return False

    else:
        return string


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
