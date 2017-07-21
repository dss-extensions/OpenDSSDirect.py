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


def to_dataframe(module, dss=None):
    if dss is None:
        import opendssdirect as dss

    data = dict()

    for e in module.AllNames():
        data[e] = dict()

    if len(data) != 0:

        for i in dss.iterator(module, 'Name'):
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
