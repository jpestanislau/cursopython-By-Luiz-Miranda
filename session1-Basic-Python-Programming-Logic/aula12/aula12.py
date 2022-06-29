"""
All elements in Python are an object.
Each object has its set of methods
"""
num1 = input('Type the first number: ')
num2 = input('Type the first second: ')

if num1.isdigit() and num2.isdigit():
    print(f'The sum of numbers: {int(num1) + int(num2)}')
else:
    print('Invalid values')
