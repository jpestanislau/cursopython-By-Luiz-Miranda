"""
Types of Data
str - string
int - integer
float - floating point
bool - boolean or logical valuer
"""

# The function "type()" returns the data type of the parameter
print('John', type('John'))
print(10, type(10))
print('10', type('10'))
print(10 == 10, type(10 == 10))
print('A' == 'a', type('A' == 'a'))  # Python is case-sensitive

# Typecast is forcing conversion from one data type to another
print('', bool(''))  # Voids string are considered false
print('L', bool('L'))  # Filled string are considered true
print(int('10') + int('10'))
print(float('10'))
# print(int('10.0')) In this case, an error message will be returned.



