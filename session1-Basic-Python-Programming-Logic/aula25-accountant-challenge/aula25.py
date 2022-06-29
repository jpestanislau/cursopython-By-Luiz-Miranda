"""
print this on screen using for or while loops
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
9 1
0 0

"""
count = 10
order1 = 0
order2 = 10

while count >= 0:
    print(order1, order2)
    order1 += 1
    order2 -= 1
    count -= 1
print('--------')
for x, y in enumerate(range(10, -1, -1)):
    print(x, y)

