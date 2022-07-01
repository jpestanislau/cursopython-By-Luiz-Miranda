"""
Functions (def) in Python - *arg (wrapped arguments)
We can use '*argument_name' in a function to set an unknown number of arguments
The arguments will be packed on a tuple
"""


def fun(*args):
    print(args)
    print(type(args))
    print(f'The first argument is:{args[0]}')
    print(f'The last argument is:{args[-1]}')
    print(f'The number of arguments is:{len(args)}')


fun(1, 3, 4, 5, 'casa')

my_list = [1, 2, 3, 4]

fun(my_list)  # Sending a packed list

fun(*my_list)  # Sending an unpacked list
