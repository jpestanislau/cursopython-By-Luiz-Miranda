"""
Dictionary Comprehension!
Syntax
    {<expression> for (key, value) in <iterable> if <condition>}
    {new_key:new_value for (key, value) in <dict>.items() if <condition>}

Use to create new dictionaries from existing dictionaries and iterables
"""

l1 = [
    ("key01", "value01"),
    ("key02", "value02"),
    ("key03", "value03"),
]

dic1 = {x: y.upper() for x, y in l1}
# print(dic1)
dic2 = {f'Key_{x}': x**2 for x in range(5)}
print(dic2)
