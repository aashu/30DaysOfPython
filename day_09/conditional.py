age = int(input('Enter your age: '))
if age>18 :
    print('u are eligible to vote.')
else :
    print('play games')

# if given user input does not exist in list, add it to list and print it
fruits = ['banana', 'orange', 'mango', 'lemon']

user_choice = input('Enter any fruit name: ')
if user_choice not in fruits:
    fruits.append(user_choice)
    print(fruits)
else:
    print(fruits)


