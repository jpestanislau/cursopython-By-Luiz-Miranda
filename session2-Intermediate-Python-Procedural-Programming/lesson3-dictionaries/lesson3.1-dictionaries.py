"""
Dictionaries in Python!

Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered (since version 3.7), changeable and do not allow duplicates.
Dictionaries are written with curly brackets.

Source: https://www.w3schools.com/python/python_dictionaries.asp

Keys can assume anytype non-mutable type (string, int, float, tuple)
"""

d1 = {'key1': 'value1', 2: 'value2', 'key3': 'value3'}

d2 = dict(key1='value1', key2='value2', key3='value3')  # Second way to create a dictionary

print(d1, type(d1))
print('---')

print('The element with "key1" as key  is', d1['key1'])  # Access a value inside a dictionary
print('---')

d1['key3'] = 'new_value3'   # Update a value
print('The element with "key3" as key  is', d1['key3'])
print(d1)
print('---')

d1['newKey'] = 'value4'  # Add an element
d1.update({'newestKey': 'value5'})  # Add an element
print(d1)
print('---')

del d1['newestKey']  # Remove an element
print(d1)
print('---')

print(d1.values())  # The ".values()" method  returns all values
if 'value4' in d1.values():
    print('In d1, exist a element with "value4" as value')
print('---')

print(d1.keys())  # The ".keys()" method  returns all keys
print('---')

print(d1.items())  # The ".keys()" method  returns a list containing a tuple for each key value pair
print('---')

if 'key6' in d1:
    print('There is!')  # If there is an element with the key "key6" in the dictionary "d1", this line will be executed

if d1.get('ke54'):  # The ".get()" method can return the element if it exists or 'None' if not
    print('There is!')  # If there is an element with the key "key5" in the dictionary "d1", this line will be executed

