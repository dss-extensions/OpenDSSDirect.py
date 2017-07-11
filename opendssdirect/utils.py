import inspect


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
