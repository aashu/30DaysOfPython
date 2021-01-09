# print the below pattern
  #
  ##
  ###
  ####
  #####
  ######
  #######

for row in range(0,7):
    while row >= 0 :
        print('#',end='')
        row -= 1
    print('') # it has end='\n' default which results in newline

libraries =  ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in libraries:
    print(item)

odd_numbers = []
even_numbers = []
for number in range(1,101):
    if number % 2 == 0 :
        even_numbers.append(number)
    else :
        odd_numbers.append(number)
print('even numbers upto 100: ', even_numbers)
print('odd_numbers upto 100: ', odd_numbers)

