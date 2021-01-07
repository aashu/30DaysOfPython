from random import randint, random
numbers = list(range(1,11))
print(numbers)
print(len(numbers))

print(numbers[0],numbers[len(numbers)-1],numbers[-1])

mixed_data_types =  ['first_name',2,123,False,2.23]
it_companies = ['facebook','google','microsoft','apple','ibm','oracle','amazon']

print(mixed_data_types)
it_companies.append('solarwinds')
print(it_companies[randint(1,7)].upper())

print('#'.join(it_companies))
it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True)
print(it_companies)

print('first three companies are ',it_companies[:3])
print('last three companies are ',it_companies[-3:])
it_companies.pop(0)
it_companies.remove('ibm')
print(it_companies)
it_companies.clear()
print(it_companies,' is empty right now')

del it_companies

# join the given lists

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)
for x in ['Python','SQL']:
    full_stack.insert(full_stack.index('Redux') + 1,x)
print(full_stack)




ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f'max is {ages[0]} and min is {ages[-1]}')

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
f,s,t = countries[:3]
rest = countries[3:]
print(f,s,t,rest)
