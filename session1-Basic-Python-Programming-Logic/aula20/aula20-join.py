"""
Join in Python

* Join - Is a String method. Merge all items into a string, using a hash character as separator. A string must be
specified as the separator.
string.join(iterable)
iterable	Required. Any iterable object where all the returned values are strings

"""
string1 = 'Brazil is the country of hope!'
my_list1 = string1.split()
string2 = '#'.join(my_list1)
print(my_list1)
print(string2)
