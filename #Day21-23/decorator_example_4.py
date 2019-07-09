def tag(tagname):
    def formatting(func):
        def wrapper(name):
            return func(name).upper()+tagname
        return wrapper
    return formatting


# return decorator_1


@tag('p')
def print_hello(name='ahmed'):
    return 'hello {}'.format(name)


print(print_hello(name='ameena'))
