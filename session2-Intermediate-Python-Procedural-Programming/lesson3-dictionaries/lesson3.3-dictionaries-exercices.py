questions = {
    'Question 1': {
        'question': 'How many is 2+2? ',
        'answers': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'right_answer': 'b',
    },
    'Question 2': {
        'question': 'How many is 3x2? ',
        'answers': {
            'a': '4',
            'b': '101',
            'c': '6',
        },
        'right_answer': 'c',
    },
}

for qk, qv in questions.items():
    print(qk, qv['question'])
    for ak, av in qv['answers'].items():
        print(f'\t[{ak}] {av}')
    user_answer = input('What your quest?')
    if user_answer == qv['right_answer']:
        print('You hit!')
    else:
        print('You miss!')
    print('---')
