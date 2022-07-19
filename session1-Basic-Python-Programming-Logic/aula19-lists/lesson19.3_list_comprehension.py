"""
List Comprehension in Python!

Creates a new list based on the values of an existing list.
    new_list = [expression for item in iterable if condition == True]
    new_list = [expression for item in iterable]

Source:
https://www.w3schools.com/python/python_lists_comprehension.asp

"""


l1 = [1, 2, 3, 4, 5, 6]

l2 = [l1_item for l1_item in l1]

l3 = [l1_item for l1_item in l1 if l1_item > 3]

l4 = [l1_item for l1_item in l1 if l1_item > 3 if l1_item < 5]

l5 = [l1_item * 4 for l1_item in l1 if l1_item > 3 if l1_item < 5]

l6 = [l1_item * 2 if l1_item > 4 else l1_item for l1_item in l1]

my_tuple = (
    ('key01', 'value01'),
    ('key02', 'value02'),
    ('key03', 'value03'),
)

l7 = [(x, y) for y, x in my_tuple]

print(l7)
