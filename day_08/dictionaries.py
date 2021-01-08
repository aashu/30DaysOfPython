dog  = dict()
dog['breed_name'] = 'Azawakh'
dog['breed_group'] = 'Hound Dogs'
dog['height_in_inch'] = 23
dog['life_span_in_years'] = 13

print(dog)
print(len(dog))
# items() return a dict_item object
print(dog.items())
print(dog.keys())
print(dog.values())
del dog['breed_name']

print(dog)

del dog