name = 'JP'
age = 25
height = 1.85
weight = 98.2
current_year = 2022
year_of_birth = current_year - age
ofAge = age >= 18
bmi = weight/(height ** 2)

print(f'{name} is {age} years old, born in {year_of_birth}, has {height} of height, has {weight} of weight and your '
      f'BMI is {bmi:.2f}')

