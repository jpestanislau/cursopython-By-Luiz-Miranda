"""
Lists in Python
append, insert, pop, del, clear, extend, +
min, max
range
"""
my_list = [23, 'jp', 3.4, True, 'car']
# print(type(my_list))
# print(my_list[3])
# print(my_list[0:4])

for element in my_list:
    print(f'The type from element is {type(element)} and your value is {element}')

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

# print(l3)

l1.extend(l2)  # Merge one list into another
# print(l1)

l2.append(7)  # Add an item to the end of the list
# print(l2)

l2.insert(2, 'Item added')  # Add an item to the select position. The new item will occupy the select index
# print(l2)

l2.pop()  # Remove an item from the list. The default parameter is -1 (the last item)
# print(l2)

del(l2[3:4])  # Remove a series of items from the list
# print(l2)

l4 = list(range(1, 10))  # list() can create a list from a iterable element
# print(l4)
# print(min(l4))  # Show the min value from a list
# print(max(l4))  # Show the max value from a list

soma = 0
for value in l4:
    soma = soma + value
    # print(f'The soma is: {soma}. And the value is: {value}')
