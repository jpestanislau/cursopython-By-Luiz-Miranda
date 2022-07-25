"""
Combinations in Python!

This method takes an iterable and an input r as an input and return an object list of tuples which
contain all possible combination of length r in a list form. The order doesn't matter.
(a, b) == (b, a)

combinations(iterable, r)
r is length subsequences of elements from the input iterable.

Source:
https://www.geeksforgeeks.org/permutation-and-combination-in-python/
https://docs.python.org/3/library/itertools.html#itertools.combinations
"""
from itertools import combinations

peoples = ['John', 'Maria', 'Sophia', 'Rafa']
comb = combinations(peoples, 2)
print(type(comb))
print(comb)
print('Combinations is a iterable:', hasattr(comb, '__iter__'))
print('Combinations is a iterator:', hasattr(comb, '__next__'))
print('')

for group in combinations(peoples, 2):
    print(group)
