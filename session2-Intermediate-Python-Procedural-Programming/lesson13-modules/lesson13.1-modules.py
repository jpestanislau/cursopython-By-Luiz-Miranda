"""
Modules in Python!
Modules are files .py with contains python codes and are used to extend the functionalities of default python language

Source:
https://docs.python.org/3/py-modindex.html
"""
import sys
from random import randint
from itertools import zip_longest as my_best_name
from itertools import count


def count(value):
    print('Haha! This function was overwritten!')


print(sys.platform)
print(randint(0, 10))
print(list(my_best_name([2, 4, 5, 6], [2, 5])))
print(count(0))
