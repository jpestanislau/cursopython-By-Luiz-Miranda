"""
Unpacking Lists in Python

"""

my_list = ['Jhon', 'Maria', 'Bruno']

n1, n2, n3 = my_list
print(n1)
print(n2)
print(n3)

# x1, x2 = my_list  # This line will return an error. There is more values than variables to unpacking

y1, *second_list = my_list
print(y1)
print(second_list)

