"""
Enumerate in Python

The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
The enumerate() function adds a counter as the key of the enumerate object.
The enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from
iterating over iterable.

enumerate(iterable, start)
iterable -> An iterable object
start -> A Number. Defining the start number of the enumerate object. Default 0

"""
string1 = 'Brazil is the country of hope!'
my_list1 = string1.split()


print(my_list1)
print(enumerate(my_list1))
print(type(enumerate(my_list1)))
print(list(enumerate(my_list1)))  # The function list() creates a list object from an iterable object

for index, value in enumerate(my_list1):
    print(f'Index: {index}. Value: {value}')
