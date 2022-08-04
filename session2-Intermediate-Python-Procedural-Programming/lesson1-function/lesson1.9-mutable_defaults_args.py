"""
PAY ATTENTION ON MULTABLE DEFAULTS ARGUMENTS IN PYTHON!

When passing a mutable value as a default argument in a function,
the default argument is mutated anytime that value is mutated.

This argument ends up having its value saved between its function calls and acts as a larger scope variable

A solution is set the arg as None.

Source:
https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/
"""


def append_list_of_clients(iterable_clients, lis=[]):
    lis.extend(iterable_clients)
    return lis


def append_list_of_clients_v2(iterable_clients, lis=None):
    if lis is None:
        lis = []
    lis.extend(iterable_clients)
    return lis


clients_01 = ['Fulano', 'Ciclano', 'Arnaldo', 'Filda']
clients_02 = ['Ivina', 'Arnald']
clients_03 = ['Maria', 'Claudia', 'Francisco']

print(append_list_of_clients(clients_01))
print(append_list_of_clients(clients_02))  # In this second  call, the return will be some with the previous

print('---')

print(append_list_of_clients_v2(clients_01))
print(append_list_of_clients_v2(clients_02))