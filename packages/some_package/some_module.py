class A:
    pass


GLOBAL_VAR = 2


def some_function():
    print('function is executing')


print('__name__ is', __name__)
if __name__ == '__main__':
    print('module has been executed')
