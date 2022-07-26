"""
Product in Python!

This method takes an iterable as an input and returns an object (iterator) of tuples that contain all products.
Cartesian product of input iterables.
The order MATTER.
    (a, b) != (b, a)
THERE IS:
    (a, a)

product(*iterables, repeat=1)
repeat is length subsequences of elements from the input iterable.

Source:
https://docs.python.org/3/library/itertools.html#itertools.combinations
"""
from itertools import product

peoples = ['John', 'Maria', 'Sophia', 'Rafa']
prod = product(peoples, repeat=2)
print(type(prod))
print(prod)
print('Product is a iterable:', hasattr(prod, '__iter__'))
print('Product is a iterator:', hasattr(prod, '__next__'))
print('')

for group in prod:
    print(group)
