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


"""
List Comprehension Exercise!
    Add up all product prices
"""
shop_car = []

shop_car.append(('Product 01', 30))
shop_car.append(('Product 02', 20))
shop_car.append(('Product 01', 50))

total = sum([value_price for value_name, value_price in shop_car])
print(total)
