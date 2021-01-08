# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('twitter')
it_companies.update(['solarwinds','redhat','infosys'])
print(it_companies)
it_companies.remove('Apple')
print(it_companies)


print(A.union(B))
print(A.intersection(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))

del age,A,B,it_companies

statement = 'I am a Student and I love to learn new things'
unique_words = set(statement.split(' '))
print(unique_words)