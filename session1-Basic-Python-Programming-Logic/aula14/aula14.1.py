num1 = input('Type the first number: ')

if num1.isdigit():
    num1 = int(num1)
    if num1%2 == 0:
        print(f'The number {num1} is pair')
    else:
        print(f'The number {num1} is odd')
else:
    print(f'The valuer "{num1}" is not a number')
