import json
import os

d1 = {
    'People_1': {
        'name': 'Luiz',
        'age': 33,
        'year': 1859
    },
    'People_2': {
        'name': 'Maria',
        'age': 33,
        'year': 1859
    },
    'People_3': {
        'name': 'John',
        'age': 33,
        'year': 1859
    }
}

d1_json = json.dumps(d1, indent=True)  # Convert the dictionary into a json

with open('abc.json', 'w+') as file:  # Save the .json in a file
    file.write(d1_json)


with open('abc.json', 'r+') as file:  # Reading the .json
    d2 = file.read()

d2 = json.loads(d2)  # Convert the json into a dictionary


for people, value in d2.items():
    print(people)
    for v1, v2 in value.items():
        print(f'\t {v1}: {v2}')


os.remove('abc.json')

