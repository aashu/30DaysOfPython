print('thirty '+ 'days '+'of ' + 'python')
slogan = 'cODiNg' + ' fOr' +' AlL'
print(len(slogan))
print(slogan.upper())
print(slogan.lower())
print(slogan.swapcase())
print(slogan.title())
print(slogan.capitalize())

print(slogan[:7])

print('coding' in slogan.lower())
print(slogan.lower().find('all'))  
print(slogan.lower().index('coding'))

print(slogan.lower().replace('coding','python'))
print(slogan.split(' '))
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

# create an abbreviation for value in variable company
token = slogan.title().split()
abbr = ''
for word in token:
    abbr += str(word[0])
print(abbr)


sentenceWithLotsOfBecause = 'You cannot end a sentence with because because because is a conjunction'

firstBecauseStartingIndex = sentenceWithLotsOfBecause.find('because');
lastBecauseStartingIndex = sentenceWithLotsOfBecause.rfind('because')
print(firstBecauseStartingIndex,' & ',lastBecauseStartingIndex)

print(sentenceWithLotsOfBecause[firstBecauseStartingIndex:(lastBecauseStartingIndex+len('because') + 1)])

print(slogan.lower().startswith('coding'))
print(slogan.lower().endswith('coding'))

slogan = '           coding      for       all      '
print(slogan.strip())

py_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(py_libraries))

print('name\t\tage\t\tcountry\nabc\t\t198\t\tanything')

