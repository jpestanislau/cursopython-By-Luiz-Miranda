"""
Function with returns!
- Functions with not 'return' defined returns a None value
- As soon as the 'return' line is executed the function will complete its life cycle
- my_function != my_function(). The function will only executed in the second case
"""


def my_function(msg='Default msg!'):
    return f'The msg is {msg}'


def division(var1, var2):
    return var1/var2


var = my_function()
print(var)

var = my_function
print(var)
