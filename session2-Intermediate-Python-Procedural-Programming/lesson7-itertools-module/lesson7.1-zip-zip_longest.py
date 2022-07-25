"""
Zip and Zip_longest in Python!

The zip() function returns a zip object, which is an iterator of tuples.
where the first item in each passed iterator is paired together,
and then the second item in each passed iterator are paired together etc.

If the passed iterators have different lengths,
the iterator with the least items decides the length of the new iterator.

Source:
https://www.w3schools.com/python/ref_func_zip.asp
"""
from itertools import zip_longest

cities = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
states = ['SP', 'MG', 'BA']
cities_states = zip(cities, states)


print('The object "cities_states" is type:', type(cities_states))
print('The object "cities_states" is iterator:', hasattr(cities_states, '__next__'))
print('')

# print(dict(cities_states))

# print(list(cities_states))


# for value in cities_states:
#     print(value)

cities_states_long01 = zip_longest(cities, states)
cities_states_long02 = zip_longest(cities, states, fillvalue='Default value')
print(list(cities_states_long01))
print(list(cities_states_long02))
