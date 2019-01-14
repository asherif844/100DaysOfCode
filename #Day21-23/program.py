# def get_profile(name, active=True, *sports, **awards):
# print('positional arguments (required): ', name)
# print('keyword arguments (not required, default values): ', active)
# print('arbitrary argument list (sports): ', sports)
# print('arbitrary keyword argument dictionary (awards): ', awards)


print(get_profile('ahmed', True, 'soccer', 'tennis',
                  pythonista='special honor of the community', topcoder='2018 Coding Champ'))


def show_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print('hi from decorator - args:')
        print(args)
        result = function(*args, **kwargs)
        print('hi again from decorator - kwargs:')
        print(kwargs)
        return result
    return wrapper


@show_args
def get_profile(name, active=True, *sports, **awards):
    print('\n\hi from the get_profile function\n')


print(get_profile('bob', True, 'basketball', 'soccer',
                  pythonista='special honor of the community', topcoder='2017 code camp'))
