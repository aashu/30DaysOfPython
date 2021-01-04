print('Day 2 of 30 Days of python Programming')
first_name = 'anonymous'
last_name = 'unknown'
full_name = first_name + last_name
country = 'marsia'
city = 'Gotham'
age = '-4'
year = '2021'
is_married = True and False
is_true = False or True
is_light_on = is_true and is_married

alpha = beta = gamma = 0

print(type(first_name))
print(type(city))
print(type(age))
print(type(year))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))
print(len(country))

# let's help circle know about itself
radius = float(input('enter radius: '))
area = 3.14 * (radius**2)
circumference = (2*area)/radius
print(f'area = {area}')
print(f'circumference = {circumference}')

help(ValueError)