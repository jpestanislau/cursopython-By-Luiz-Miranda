"""
Functions - def
"""


def function_name():
    print('Hello World!')


def function_with_parameters(msg):
    print(msg)


def optional_parameters(msg='This parameter is optional and has a default value'):
    print(msg)


function_name()
function_with_parameters('My msg!')
optional_parameters('Setting parameter')
optional_parameters()
