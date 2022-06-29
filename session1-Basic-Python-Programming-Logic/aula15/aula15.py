"""
Formatting values with modifiers

:s - Text (strings)
:d - Integers (int)
:f Floating point numbers (float)
:.(NUMBER)f - Number of decimal places (float)
:(CHARACTER)(> or < or ^)(QUANTITY)(type -s, d, or f)

> - Left
< - Right
^ - Center
"""

num_1 = 10
num_2 = 3
division = num_1 / num_2
print('The value is {:.2f}'.format(division))
print(f'The value is {division:.2f}')

num_3 = 1155
print(f'{num_3:0>10}')
print(f'{num_3:0>10.2f}')

name = 'JP'
print(f'{name:#^12}')  # I want my string to be 12 characters in total and the missing characters to be '#' and the
# original string to be in the middle '^'
