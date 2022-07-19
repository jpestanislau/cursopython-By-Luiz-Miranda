"""
List Comprehension Exercise!
    Take string value and separate by dot every repetition
"""
str1 = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
step = 10

list1 = [str1[x: x + step] for x in range(0, len(str1), step)]
list2 = '.'.join(list1)
print(list1)
print(list2)
