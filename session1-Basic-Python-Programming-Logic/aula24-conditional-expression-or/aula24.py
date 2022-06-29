"""
Conditional expression with or
"""
name = input('Type your name: ')
print(name or 'You did not type!')


a = 0
b = None
c = False
d = []
e = {}
f = 'Luiz'
g = 12

msg = a or b or c or d or e or f or g  # Check the first true value and assign it to the variable
print(msg)
