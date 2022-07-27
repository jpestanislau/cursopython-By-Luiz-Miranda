"""
Learning about map in Python!

The map() function executes a specified function for each item in an iterable.
The item is sent to the function as a parameter.
    map(function, iterables)
        function	Required. The function to execute for each item
        iterable	Required. A sequence, collection or an iterator object. You can send as many iterables as you like,
                    just make sure the function has one parameter for each iterable.

The return is an iterator object that references the iterable passed as a parameter.
Source:
https://www.w3schools.com/python/ref_func_map.asp
"""
from data import people, products, l1


def increase_prices(product):
    product['price'] = round(product['price'] * 1.5, 2)
    return product


def increase_age(person):
    person['age'] = person['age'] + 3
    return person


l2 = map(lambda x: x*2, l1)
# l2 = [x * 2 for x in l1]
# print(list(l2))

print('In products, the first product:', products[0])
print('')

new_products = list(map(increase_prices, products))

for item in new_products:
    print(item)

print('')

print('In products:', products[0])
new_products[0]['name'] = 'SD Card'
print('In products:', products[0])
print('In new_products:', new_products[0])

print('products == new_products: ', products == new_products)
print('')


older_people = list(map(increase_age, people))
print(older_people)

