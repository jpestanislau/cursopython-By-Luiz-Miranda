def convert_to_number(value):
    try:
        value = int(value)
        return value
    except ValueError:
        try:
            value = float(value)
        except ValueError:
            pass


my_number = convert_to_number(input('Type a number'))

if my_number is None:
    print('You do not type a number')
else:
    print(my_number * 5)
