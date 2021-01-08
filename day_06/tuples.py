empty = ()

random_names1 =('alan', 'smith','john','frank')
random_names2 = ('himanshu','mahesh','ramesh')
random_names = random_names1 + random_names2

print(random_names)

# random_names[3] = 'bill' #error

# convert to list and then change value
random_names = list(random_names)
random_names[3] = 'bill'
random_names = tuple(random_names)
print(random_names)

# unpacking tuples
a,b,c,d = random_names1
print(a,b,c,d)

# slicing
print(random_names[:-1])

del random_names

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries,'Iceland' in nordic_countries)
