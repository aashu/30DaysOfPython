def compare_numbers(first,second):
    return first < second

print(compare_numbers(second = 4,first = 3))

def add(*args):
    total = 0
    for num in args:
        total += num
    return total
print(add(2,2,2,23,4,2,2,3))


# you live in an imaginary country, arbitrary assing following season in group of 3 months
seasons = ['Autumn','Winter','Spring','Summer']
month_number =  int(input('Enter month number(1-12): '))

print(seasons[month_number//3])


