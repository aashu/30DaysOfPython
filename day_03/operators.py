age = 4
not_my_height = 175
complex_variable = 2+2j


# Area of Triangle (ignore validation)
base = float(input('Enter base: '))
height = float(input('Enter height: '))
print('The area of the triangle is: ',base*height*0.5)

# perimeter of trianglef
a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))
print('The perimeter of the triangle is ',a+b+c)

print(len('python') != len('jargon'))
print('on' in 'python' and 'on' in 'jargon')

statement =  'lets hope this course is not full of jargon'
print('jargon' in statement)



print('lets find out how many second you had survived (precision is upto years only)')
year = int(input('enter no of years: '))
print(f'u have survived for {year*12*30*24*3600}')


#     Write a python script that displays the following table

# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for i in range(1,6):
    print(i,end=' ')
    for j in range(0,4):
        print(i**j,end=' ')
    print('\n')
