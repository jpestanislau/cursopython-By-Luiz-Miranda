name= 'JP'
age = 25
height = 1.85
weight = 98
ofAge = age >= 18
bmi = weight/(height ** 2)

print('Name:', name)
print('Age:', age)
print('Height:', height)
print('Is of age:', ofAge)


print(name, 'is', age, 'years old and your BMI is', weight/(height ** 2))

# f-strings is an alternative to concatenate variables within a string
# ":.nf" is a way to set the number of decimal places after the floating point where n is a number of places desired
print(f'{name} is {age} years old and your BMI is {bmi:.2f}')

# ".format()" is an another alternative to concatenate variables within a string
print('{} is {} years old and your BMI is {:.2f}'.format(name, age, bmi))
print('{0} is {1} years old and your BMI is {2:.2f}'.format(name, age, bmi))
print('{0} {0} is {1} years old and your BMI is {2:.2f}'.format(name, age, bmi))
print('{n} is {a} years old and your BMI is {b:.2f}'.format(n=name, a=age, b=bmi))
print('{b:.2f} {n} is {a} years old and your BMI is {b:.2f}'.format(n=name, a=age, b=bmi))
