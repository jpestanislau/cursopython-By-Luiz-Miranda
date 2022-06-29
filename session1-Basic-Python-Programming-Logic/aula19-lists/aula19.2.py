"""
Gaming - Hit the secret word!
"""
secret = 'perfume'
list_of_hits = []

while True:
    hint = input('Type a single character:')

    #  Multi-character check
    if len(hint) > 1:
        print('You type more the one character!')
        continue

    # Check of a hit
    if hint in secret:
        print(f'You hit one letter! The character "{hint}" exist in the secret')
        list_of_hits.append(hint)
    else:
        print(f'You miss! The character "{hint}" do not exist in the secret!')

    # Letter by Letter comparison
    secret_temp = ''
    for letter in secret:
        if letter in list_of_hits:
            secret_temp += letter
        else:
            secret_temp += '*'

    # Check if the secret was hit
    if secret_temp == secret:
        print(f'YOU WIN! The secret is: "{secret_temp}"')
        break
    else:
        print(f'Try again... Tip: "{secret_temp}"')
