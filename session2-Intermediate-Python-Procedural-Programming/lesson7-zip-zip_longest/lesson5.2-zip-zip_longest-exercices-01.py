"""
Exercising Zip and List Comprehension

Considering two lists of integers or floats (list A and list B)
Sum the values in the lists returning a new list with the summed values:
If one list is larger than the other, the sum will only consider the size of the list.
smaller.

Example:
list_a     = [1, 2, 3, 4, 5, 6, 7]
list_b     = [1, 2, 3, 4]

list_sum = [2, 4, 6, 8]

"""

list_a = [10, 2, 3, 40, 5, 6, 7]
list_b = [1, 2, 3, 4]

# The Python way
list_sum_01 = [x + y for x, y in zip(list_a, list_b)]
# print(list_sum_01)

# Non Python Way
list_sum_02 = []
for i in range(len(list_b)):
    list_sum_02.append(list_a[i] + list_b[i])

# print(list_sum_02)
