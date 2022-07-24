"""
count (from itertools) on Python!!!

Makes an iterator that returns values that counts up or down INFINITELY.
    count(start=0, step=1)
Source:
https://note.nkmk.me/en/python-itertools-count-cycle-repeat/
https://docs.python.org/3/library/itertools.html#itertools.count
"""
from itertools import count

# my_couter = count()
#
# for value in my_couter:
#     print(value)
#     if value >= 55:  # Limiter
#         break
#
# my_couter = count(start=10, step=2)
#
# for value in my_couter:
#     print(value)
#     if value >= 20:  # Limiter
#         break

list_count = count()
names = ['Joana', 'Paula', 'Francisca']
names = zip(names, list_count)
print(list(names))
