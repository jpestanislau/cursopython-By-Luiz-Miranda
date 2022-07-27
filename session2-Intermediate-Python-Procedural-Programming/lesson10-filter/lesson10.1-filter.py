"""
filter in Python!

Returns an iterator were the items are filtered through a function to test if the item is accepted or not.
The filter function must return false or true
    filter(function, iterable)
        function	A Function to be run for each item in the iterable
        iterable	The iterable to be filtered

Source:
https://www.w3schools.com/python/ref_func_filter.asp
"""
from data import people, products, l1

l2 = filter(lambda item: item > 5, l1)

print(list(l2))
l3 = [item for item in l1 if item > 5]
print(l3)
