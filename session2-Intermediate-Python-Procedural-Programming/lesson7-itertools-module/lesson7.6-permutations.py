"""
Permutations in Python!

This method takes an iterable as an input and returns an object (iterator) of tuples that contain all permutations.
The order MATTER.
    (a, b) != (b, a)

permutations(iterable, r)
r is length subsequences of elements from the input iterable.
If r is not specified or is None, then r defaults to the length of the iterable and all possible full-length
permutations are generated.

Source:
https://www.geeksforgeeks.org/permutation-and-combination-in-python/
https://docs.python.org/3/library/itertools.html#itertools.permutations
"""
from itertools import permutations

peoples = ['John', 'Maria', 'Sophia', 'Rafa']
perm = permutations(peoples, 2)
print(type(perm))
print(perm)
print('Permutations is a iterable:', hasattr(perm, '__iter__'))
print('Permutations is a iterator:', hasattr(perm, '__next__'))
print('')

for group in perm:
    print(group)
