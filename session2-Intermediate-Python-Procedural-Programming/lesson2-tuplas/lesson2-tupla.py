"""
Tuple in Python!

Tuples are like list, but they are unchangeable
Tuples are written with round brackets

Source: https://www.w3schools.com/python/python_tuples.asp
"""

t1 = (1, 2, 3, 4, 'a', 2.5)

t2 = 1, 2, 3, 4, 'a', 2.5   # This is also a tuple

t3 = 'a',  # This is also a tuple. A tuple

t4 = t1 + t2 + t3   # Tuple can be concatenated

n1, n2, *n3, nLast = t4  # Unpacking a tuple

t5 = (1, 3) * 3  # Tuples can be multiplied

l1 = list(t5)  # Tuples can be typeCast to a list
l1 = tuple(l1)  # Contrariwise too

for var in t1:  # Show all elements from a tuple
    print(var)

print('---')
print(t1[2:])   # Slicing a tuple
print('---')
