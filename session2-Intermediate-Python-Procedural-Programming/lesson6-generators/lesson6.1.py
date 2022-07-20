"""
Generators in Python!

A generator is a function that returns an iterator object which we can iterate over ONE VALUE AT A TIME.
Generator function must use "yield" statements instead of a "return" statements.

A "return" statement terminates a function entirely.
A "yield" statement pauses the function saving all its states and later continues from there on successive calls.

Generators help save memory when creating very large iterator objects.

Source:
https://www.programiz.com/python-programming/generator

"""
import sys
import time


def gen(*args):
    if args:
        for n in range(args[0]):
            yield n
    else:
        for n in range(1000):
            yield n


gen01 = gen(10)
print('The gen01 object type is:', type(gen01))
print('The gen01 object is a iterable:', hasattr(gen01, '__iter__'))
print('The gen01 object is a iterator:', hasattr(gen01, '__next__'))
print('')

# for x in gen01:
#     print(x)

l1 = [x for x in range(1000)]
gen02 = (x for x in range(1000))

print('The list l1 size is:', sys.getsizeof(l1))
print('The generator gen02 size is:', sys.getsizeof(gen02))
