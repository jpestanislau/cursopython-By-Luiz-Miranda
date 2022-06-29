"""
The command input returns a str valuer from the user via prompt
"""

var1 = input("Please, type your name: ")
var2 = input("Please, type your age: ")
print('The name typed was:', var1, 'and', 'this valuer is an', type(var1))
print(f'{var1} was born in {2022-int(var2)}')

