"""
Exercise:
    Create a function that finds the first duplicate considering the second number as doubling.
    Return the considered duplication.

Extra Data:
    It is a list of lists of integers
    Internal lists are 10 elements long
    Internal lists contain numbers between 1 to 10 and they can be duplicated

Requirements:
    The order of the duplicate number is considered from the second occurrence of the number, that is, the duplicated
    number itself.

Example:
    [1, 2, 3, ->3<-, 2, 1] -> 1, 2 and 3 are doubled (return 3)
    [1, 2, 3, 4, 5, 6] -> Return -1 (no duplicates)
    If no duplicates are found in the list, yields -1
"""

integer_list = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def duplicate_list_check(param_integer_list):
    param_integer_list_order = param_integer_list.copy()
    param_integer_list_order.sort()
    li = list(set(param_integer_list_order))
    if param_integer_list_order != li:
        print(f'The list {param_integer_list} have a duplicate value')

        previous_values = set()
        for value in param_integer_list:
            if value in previous_values:
                print(f'The first occurrence of a duplication is: {value}')
                print('---')
                break
            previous_values.add(value)
    else:
        print(f'The list {param_integer_list} NOT have a duplicate value')


def find_first_duplicate_by_luizomf(param_integer_list):
    checked_numbers = set()
    first_double = -1

    for number in param_integer_list:
        if number in checked_numbers:
            first_double = number
            break

        checked_numbers.add(number)

    return first_double


for x in integer_list:
    duplicate_list_check(x)

# for x in integer_list:
#     find_first_duplicate_by_luizomf(x)
