hour = input('Type what time is it in an integer: ')

if hour.isdigit():
    hour = int(hour)
    if 0 <= hour <= 11:
        print('Good morning!')
    elif 12 <= hour <= 17:
        print('Good afternoon!')
    elif 18 <= hour <= 23:
        print('Good afternoon!')
    else:
        print(f'The valuer "{hour}" is not a valid time')
else:
    print(f'The valuer "{hour}" is not a integer')
