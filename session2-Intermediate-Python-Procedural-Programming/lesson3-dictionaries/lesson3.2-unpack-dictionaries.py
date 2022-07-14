d1 = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}

for k in d1:  # This will only print the keys of all elements
    print(k)

print('---')

for k in d1.values():  # This will only print the values of all elements
    print(k)

print('---')

for k in d1.items():
    print(k)

print('---')

for k in d1.items():
    print(k[0], k[1])

print('---')

for k, v in d1.items():
    print(k, v)

clients = {
    'client1': {
        'name': 'Maria',
        'last-name': 'Fulana'
    },

    'client2': {
        'name': 'Claudia',
        'last-name': 'Correia'
    },

    'client3': {
        'name': 'Fualana',
        'last-name': 'Assada'
    },

}

for client_k, clients_v in clients.items():
    print(f'Showing {client_k}')
    for data_k, data_v in clients_v.items():
        print(f'\t{data_k} = {data_v}')
