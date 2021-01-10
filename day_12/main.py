from random import random,randint
import string
from math import pi,ceil,floor,log10,pow,sqrt
from statistics import *
import sys
import os
from my_module import generate_full_name as gfn

print(gfn('alfred','obama'))


os.chdir('day_12')
print(os.getcwd())

print(f'script name : {sys.argv[0]}')
for parameter in sys.argv :
    print(parameter)


# exit the program with parameter as exit code
#sys.exit(23)

ages = list(range(20,80,3))
ages.append(26)
print(f'ages : {ages}')
print('mean :',mean(ages))
print('median : ',median(ages))
print('mode: ',mode(ages))
print('std deviation: ',stdev(ages))

# maths module functions
print('maths ahead!')
print(pi)
print(sqrt(2))
print(pow(2,3))
print(ceil(9.8))
print(floor(9.81))
print(round(9.81),round(9.21))
print(log10(100))

#string
print('string module methods')

print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

# random
print('random')

print(random())
print(randint(12,13))