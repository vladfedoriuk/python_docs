import functools


def decorator(cls):
    class Decorator(object):

        def __init__(self, value):
            functools.update_wrapper(self, cls)
            if isinstance(value, cls):
                self.obj = value
            elif isinstance(value, Decorator):
                self.obj = value.obj
            else:
                self.obj = cls(value)

        def __add__(self, other):
            print('Addition operation\n{} + {} = {}'.format(self, other, self.obj + other.obj))
            return Decorator(self.obj + other.obj)

        def __mul__(self, other):
            print('Multiplication operation\n{} * {} = {}'.format(self, other, self.obj * other.obj))
            return Decorator(self.obj * other.obj)

        def __truediv__(self, other):
            print('Division operation\n{} / {} = {}'.format(self, other, self.obj / other.obj))
            return Decorator(self.obj / other.obj)

        def __str__(self):
            return '({} containing {})'.format(cls.__name__, self.obj.value)

        def __call__(self):
            raise NotImplemented()

    return Decorator


@decorator
class MathObject:
    """Class representing math objects"""

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MathObject(self.value + other.value)

    def __mul__(self, other):
        return MathObject(self.value * other.value)

    def __truediv__(self, other):
        return MathObject(self.value / other.value)

    def __call__(self):
        raise NotImplemented()


def timeit(function):
    def inner(*args, **kwargs):
        import datetime
        start = datetime.datetime.now()
        res = function(*args, **kwargs)
        end = datetime.datetime.now()
        print('Elapsed time is {} [secs]'.format(end - start))
        return res

    return inner


def time_all(cls):
    class TimeAll(object):
        def __init__(self, *args, **kwargs):
            self.obj = cls(*args, **kwargs)

        def __getattribute__(self, item):
            try:
                x = super(TimeAll, self).__getattribute__(item)
            except AttributeError:
                pass
            else:
                return x
            x = self.obj.__getattribute__(item)
            if isinstance(x, type(self.obj.__init__)):
                return timeit(x)
            else:
                return x

    return TimeAll


@time_all
class SomeClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc(self, val):
        import time
        time.sleep(3)
        return (self.a + self.b) * val


a = MathObject(2)
b = MathObject(3)
c = a + b
print(c)
c = c * a
print(c)
print(MathObject.__module__)
print(MathObject.__name__)
print(MathObject.__doc__)

print(c.__doc__)
print(c.__module__)
print(c.__name__)

s = SomeClass(1, 2)
print(s.a)
print(s.b)
print(s.calc(3))
print(type(c.__init__))
