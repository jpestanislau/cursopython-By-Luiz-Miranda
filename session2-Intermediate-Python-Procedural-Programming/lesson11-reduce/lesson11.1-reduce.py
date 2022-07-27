"""
reduce in Python!

Apply function of two arguments cumulatively to the items of iterable,
from left to right, so as TO REDUCE THE ITERABLE TO A SINGLE VALUE.
    reduce(function, iterable, [initializer])
        [initializer] is the initial value from accumulator
Source:
https://docs.python.org/3/library/functools.html#functools.reduce
"""

from data import products, people, l1
from functools import reduce

# Old way
accumulator = 0
for item in l1:
    accumulator += item
print('The l1 was reduce to:', accumulator)

sum_l1 = reduce(lambda accum, value: value + accum, l1, 0)
print('The l1 was reduce to:', sum_l1)

sum_prices = reduce(lambda accum, product: product['price'] + accum, products, 0)
print('The sum of all product is:', sum_prices)
