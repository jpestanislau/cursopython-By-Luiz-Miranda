"""
Lambda Functions on Python!

A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
Source: https://www.w3schools.com/python/python_lambda.asp
"""

a = lambda x, y: x * y

print(a(2, 2))

my_list = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 18],
    ['P5', 50]
]

my_list.sort(key=lambda item: item[1])
print(my_list)
