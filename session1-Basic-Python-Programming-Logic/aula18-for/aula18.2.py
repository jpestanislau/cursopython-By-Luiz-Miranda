"""
For / Else in Python
"""

my_list = ['Claudia', 'Fernando', 'Angela', 'João']

for name in my_list:
    print(name)
    if name.lower().startswith('j'):  # The method startswith return True if the string starts with the specified value
        break
else:
    print('This snippet will not be executed if "break" command act')
