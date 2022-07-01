"""
List of exercises about Functions
"""


# First
def greeting(var='Hello!',name='dude!'):
    print(f'{var},{name}')


# Second
def my_sum(var1,var2,var3):
    return var1 + var2 + var3


# Third
def sum_of_a_percentage(var1, var2):
    print(f'You solicited 1{var2}% from {var1}')
    return var1*(1 + var2/100)


# Fourth
def fizz_buzz(var):
    if not var % 3 and not var % 5:
        return 'FizzBuzz'
    elif not var % 3:
        return 'fizz'
    elif not var % 5:
        return 'buzz'
    return 'invalid number'


print(sum_of_a_percentage(10, 30))
print(fizz_buzz(7))
