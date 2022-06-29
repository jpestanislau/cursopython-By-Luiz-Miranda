"""
Split in Python

* Split - Divide a string into a list.
    split(separator, maxsplit)
    separator	Optional. Specifies the separator to use when splitting the string. By default, whitespace is a separator
    maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
"""
string = 'Brazil is the country of hope, Brazil will survive!'
my_list1 = string.split(' ')

# Count how many times a word appears in the parse
for word in my_list1:
    print(f'The word "{word}" appears {my_list1.count(word)} times')


my_list2 = string.split(',')
print(my_list2)
