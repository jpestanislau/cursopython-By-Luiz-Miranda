"""
Groubby in Python!

Make an iterator that returns consecutive keys and groups from the iterable.
The key is a function computing a key value for each element.
The iterable needs to already be sorted on the same key function.
    groupby(iterable, key=None)

Source:
https://docs.python.org/3/library/itertools.html#itertools.groupby
"""
from itertools import groupby, tee

students = [
    {'nome': 'Luis', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'Joao', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'Andre', 'nota': 'C'},
    {'nome': 'Anderson', 'nota': 'B'},
]


def ordena(item):
    return item['nota']


students.sort(key=ordena)
grouped_students = groupby(students, ordena)

for grouping, grouped_values in grouped_students:
    values = list(grouped_values)
    print(f'Grouping: {grouping}')

    for students in values:
        print(f'\t{students}')
    print(f'Number of students in this group: {len(values)}')
    print('')


