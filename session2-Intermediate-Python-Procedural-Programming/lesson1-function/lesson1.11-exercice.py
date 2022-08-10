"""
CNPJ VALIDATION!

04,252,011/0001-10 40,688,134/0001-61 71,506,168/0001-11 12,544,992/0001-05

0 4 2 5 2 0 1 1 0 0 0 1
5 4 3 2 9 8 7 6 5 4 3 2
0 16 6 10 18 0 7 6 0 0 0 2 = 65
Formula -> 11 - (65% 11) = 1
First digit = 1 (If the digit is greater than 9, it becomes 0)

0 4 2 5 2 0 1 1 0 0 0 1 1 X
6 5 4 3 2 9 8 7 6 5 4 3 2
0 20 8 15 4 0 8 7 0 0 0 3 2 = 67
Formula -> 11 - (67 % 11) = 10 (As the result is greater than 9, so it is 0)
second digit = 0

New CNPJ + Digits = 04.252.011/0001-10
Original CNPJ = 04.252.011/0001-10
Valid

recap
543298765432 -> First digit
6543298765432 -> Second digit
"""


def remove_dots(value):
    value = value.replace('.', '')
    value = value.replace(',', '')
    value = value.replace('-', '')
    value = value.replace('/', '')
    value = value.replace(' ', '')
    return value


def test_len(value):
    if len(value) == 14:
        return True
    return False


def is_only_digit(value):
    return value.isdecimal()


def is_valid_to_test(value):
    value = remove_dots(value)
    if not test_len(value):
        return False
    if not is_only_digit(value):
        return False
    return value


def is_valid(value):
    value = list(value)
    value.pop()
    value.pop()
    lis1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    lis2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    calc = 0
    accu = 0
    pro = 0

    for x in range(len(lis1)):
        a = lis1[x]
        b = int(value[x])
        accu += lis1[x] * int(value[x])

    calc = 11 - (accu % 11)
    first_digit = calc if calc <= 9 else 0
    value.append(str(first_digit))

    accu = 0
    for x in range(len(lis2)):
        accu += lis2[x] * int(value[x])
    calc = 11 - (accu % 11)
    second_digit = calc if calc <= 9 else 0
    value.append(str(second_digit))

    if value == list(edited_cnpj):
        return True
    return False


while True:
    cnpj_entered = input('Type the CNPJ: ')
    edited_cnpj = is_valid_to_test(cnpj_entered)
    if edited_cnpj:
        print(is_valid(edited_cnpj))
