"""
CPF Generator
"""
from random import randint

new_cpf = str(randint(000000000, 999999999))
reverse = 10  # Auxiliary variable to make the check (10-2)
total = 0

for index in range(19):  # We going to make 19 loops (0,18). Nine to the first check digit and ten for the second
    if index > 8:  # Resetting index after first scan
        index -= 9

    total += int(new_cpf[index]) * reverse

    reverse -= 1

    if reverse < 2:  # End of first scan
        reverse = 11  # Resetting reverse after first scan (10:2). The second scan is (11:2)

        # Calculation of check number
        d = 11 - (total % 11)
        if d > 9:
            d = 0

        new_cpf += str(d)  # Add the correct check number to new CPF. First the tenth, second the eleventh
        total = 0  # Resetting total after first scan


print(new_cpf)
