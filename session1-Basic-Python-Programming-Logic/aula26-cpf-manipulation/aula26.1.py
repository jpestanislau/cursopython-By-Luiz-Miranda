"""
Challenge: Receive a CPF and validate it

Ex: 168.995.350-09
"""
cpf_receive = input('Type the CPF:')
cpf_receive_list = list(cpf_receive)
valid = True

# . and - check and removal
for var in cpf_receive_list:
    if var == '.' or var == '-':
        cpf_receive_list.remove(var)

# Length check
if len(cpf_receive_list) > 11 and valid:
    print('The value typed is too long.')
    print(f'The value "{cpf_receive}" is not a valid CPF')
    valid = False
elif len(cpf_receive_list) <= 10 and valid:
    print('The value typed is too short.')
    print(f'The value "{cpf_receive}" is not a valid CPF')
    valid = False


if valid:
    for var in cpf_receive_list:
        # Special characters check
        if not var.isalnum():
            print('The value has special characters.')
            print(f'The value "{cpf_receive}" is not a valid CPF')
            valid = False
            break
        # Letters characters check
        elif var.isalpha():
            print('The value has letters.')
            print(f'The value "{cpf_receive}" is not a valid CPF')
            valid = False
            break


# Last check for begin
if valid:
    print('Ready to go!')
    fist_check_digit_receive = int(cpf_receive_list[-2])
    second_check_digit_receive = int(cpf_receive_list[-1])
    cpf_receive_list_edit = cpf_receive_list
    cpf_receive_list_edit.pop()
    cpf_receive_list_edit.pop()

    # Check Fist check digit
    aux = 10
    accumulator = 0
    for var in cpf_receive_list_edit:
        if aux >= 2:
            var = int(var)
            accumulator = accumulator + (var * aux)
            aux -= 1
        else:
            break

    aux2 = 11 - (accumulator % 11)
    if aux2 > 9:
        fist_check_digit_valid = 0
    else:
        fist_check_digit_valid = aux2

    cpf_receive_list_edit.append(fist_check_digit_valid)

    # Check Second check digit
    aux = 11
    accumulator = 0
    for var in cpf_receive_list_edit:
        if aux >= 2:
            var = int(var)
            accumulator = accumulator + (var * aux)
            aux -= 1
        else:
            break

    aux2 = 11 - (accumulator % 11)
    if aux2 > 9:
        second_check_digit_valid = 0
    else:
        second_check_digit_valid = aux2

    # The final test!
    if fist_check_digit_valid == fist_check_digit_receive and second_check_digit_valid == second_check_digit_receive:
        print(f'The value "{cpf_receive}" IS a valid CPF!!!')
    else:
        cpf_receive_list.append(second_check_digit_valid)
        print(f'The value "{cpf_receive}" is not a valid CPF')
        print(f'A valid alternative is: {str(cpf_receive_list_edit)}')
