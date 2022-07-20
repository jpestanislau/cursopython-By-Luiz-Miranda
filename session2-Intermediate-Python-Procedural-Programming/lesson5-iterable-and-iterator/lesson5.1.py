"""
Iterable in Python!

An Iterable is basically an object that any user can iterate over.
All  Iterable have the "__iter__" method
Not every iterable is an iterator.

An Iterator is also an object that helps a user in iterating over another object (that is iterable).
All  Iterator have the "__next__" method.
Every iterator is basically iterable.


hasattr() - Function returns True if the specified object has the specified attribute, otherwise False.
iter() - Method returns an iterator for the given argument.

Source:
https://byjus.com/gate/difference-between-iterable-and-iterator-in-python/

"""

l1 = [1, 2, 3, 4, 5, 'car']
l2 = iter(l1)
n1 = 13

print('The int  "n1" is a iterable object:', hasattr(n1, '__iter__'))
print('The int  "n1" is a iterator object:', hasattr(n1, '__next__'))
print("")

print('The list "l1" is a iterable object:', hasattr(l1, '__iter__'))
print('The list "l1" is a iterator object:', hasattr(l1, '__next__'))
print("")

print('The list "l2" is a iterable object:', hasattr(l2, '__iter__'))
print('The list "l2" is a iterator object:', hasattr(l2, '__next__'))
print("")

print('Using "__next__" method from list l2:')
print(l2.__next__())
print(l2.__next__())
print(l2.__next__())
print(l2.__next__())
