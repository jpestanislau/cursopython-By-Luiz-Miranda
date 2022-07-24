"""
Exercising Zip and List Comprehension

Considering two lists of integers or floats (list A and list B)
Sum the values in the lists returning a new list with the summed values:
If one list is larger than the other, the sum will only consider the size of the LAGER list.

Example:
list_a     = [1, 2, 3, 4, 5, 6, 7]
list_b     = [1, 2, 3, 4]

list_sum = [2, 4, 6, 8, 5, 6, 7]

"""
from itertools import zip_longest


list_a = [10, 2, 3, 4, 5]
list_b = [12, 2, 3, 6, 50, 60, 70]

# The Python way
list_sum_01 = [x + y for x, y in zip_longest(list_a, list_b, fillvalue=0)]
print(list_sum_01)
