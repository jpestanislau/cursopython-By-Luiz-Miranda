while True:
    num1 = input('Type the first number: ')
    num2 = input('Type the second number: ')
    mode = input('Type the operation: ')

    if not num1.isdigit() or not num2.isdigit():
        print('Inputs not valid')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if mode == '+':
        print(f'The result is: {num1 + num2}')
    elif mode == '-':
        print(f'The result is: {num1 - num2}')
    elif mode == '*':
        print(f'The result is: {num1 * num2}')
    elif mode == '/':
        print(f'The result is: {num1 / num2}')
    else:
        print('Operation not valid')

    out = input('Do you want exit? [y]es or [n]o')

    if out == 'y':
        break
