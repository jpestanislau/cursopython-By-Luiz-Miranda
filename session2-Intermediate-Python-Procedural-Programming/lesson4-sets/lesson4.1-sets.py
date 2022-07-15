"""
Sets on Python!
A set is one of 4 built-in data types in Python used to store collections of data.
- Is Unordered: Don't have an index and their position can change.
- Is Unchangeable: You can't change a value already set. But you can add or remove a value.
- Don't have duplicates: All duplicates values will be ignored.
- Support Mathematical Operations: Like union, intersection, difference, and symmetric difference.
    union: |
    intersection: &
    difference: -
    symmetric difference: ^
- Some supported methods
    add()
    update()
        Will interact an element Ex: my_set.update('car') -> {'c', 'a', 'r'}
    clear()
    discard()

Source:
https://docs.python.org/3/tutorial/datastructures.html#sets
https://www.w3schools.com/python/python_sets.asp
"""

fruits = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
fruits.add('grape')  # Add an element
fruits.discard('apple')  # Removing an element
# print(type(fruits))
for x in fruits:
    print(x)

car = set('honda')  # This will construct a set with character as an element
for x in car:
    print(x)

s1 = {1, 2, 3, 4, 5, 8}
s2 = {1, 2, 3, 4, 5, 10}
s3 = set()  # Creating a void set

print(s1 | s2)  # Numbers in s1 or s2 or both
print(s1 - s2)  # Numbers in s1 but not in s2
print(s2 - s1)  # Numbers in s2 but not in s2
print(s1 & s2)  # Numbers in both s1 and s2
print(s1 ^ s2)  # Numbers in s1 or s2 but not both

# TypingCast
my_list = list(s1)
my_set = set(my_list)
