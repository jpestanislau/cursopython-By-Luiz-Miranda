name = input('Type your name: ')


if len(name) <= 4:
    print('Short name')
elif 5 <= len(name) <= 6:
    print('Median name')
elif len(name) >= 7:
    print('Long name')
else:
    print(f'The valuer "{name}" is not valid')
