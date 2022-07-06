"""
Functions (def) in Python - *kwarg (wrapped arguments)
We can use '**argument_name' in a function to set an unknown number of key arguments (name=value)
The arguments will be packed on a dict
"""


def fun(*args, **kwargs):
    print(f'The args are:{args}')
    print(type(args))
    print(f'The first argument is:{args[0]}')
    print(f'The last argument is:{args[-1]}')
    print(f'The number of arguments is:{len(args)}')

    print('-----')

    print(f'The key args are:{kwargs}')
    print(type(kwargs))
    print(f'The number of key arguments is:{len(kwargs)}')

    var = kwargs.get('name')  # A good way to check if value exist
    if var:
        print(f'There is a key argument named "name" and its value is "{var}"')
        print(f'Your type is {type(var)}')
    else:
        print(f'There is NOT a key argument named "name"')
        print(f'The default type is {type(var)}')


def fun2(**kwargs):
    print('Data type of argument: ', type(kwargs))
    for key, value in kwargs.items():
        print(f'{key} is {value}')


my_list = [1, 2, 3, 4]
# fun(my_list, name='Luis', last_name='Carlos')
fun2(name='Luis', last_name='Carlos', age=19)


