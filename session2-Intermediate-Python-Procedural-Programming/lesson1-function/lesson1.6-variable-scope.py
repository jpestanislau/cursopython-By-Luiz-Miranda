"""
Scope on Python!
"""
global_variable ='value'


def func1():
    local_variable = 'value2'
    print(global_variable)
    print(local_variable)


def func2():
    global_variable = 'another value'   # In this case, is being created a new variable independent of the first one
    print(global_variable)


def func3():
    # Using the keyword "global" before the previously declared global variable, it is possible to change it in local
    # scope
    global global_variable
    global_variable = 'This is not a good practice. Prefer to use arguments'
    print(global_variable)


def func4():
    print(local_variable)  # This line will cause an error. "local_variable"


func1()
func2()
print(global_variable)
func3()
