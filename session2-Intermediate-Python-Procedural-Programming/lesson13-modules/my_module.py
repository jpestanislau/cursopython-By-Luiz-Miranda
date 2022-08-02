import math

PI = math.pi


def double_list_values(l):
    return [x*2 for x in l]


def multiply_list_values(l):
    value = 0
    for index in l:
        value *= index
    return value


if __name__ == '__main__':
    print('This block will execute only if "my_module.py" will execute. No with it will import')

print(f'The module {__name__} was imported')
