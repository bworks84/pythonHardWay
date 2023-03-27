# Dictionaries

# Refresher
things = ['a', 'b', 'c', 'd']
# print(things[1])  # b
things[1] = 'z'
# print(things)  # ['a', 'z', 'c', 'd']

# You can only use numbers to get items out of lists
# A dict lets you use anything to get items out of a list

stuff = {'name': "Zed", 'age': 36, 'height': 6*12+2}
print(stuff)
print(stuff['name'])
print(stuff['age'])
stuff['city'] = 'Winston-Salem'

# can also manipulate

stuff[1] = 'Wow'
print(stuff[1])  # 'Wow'
print(stuff)
#{'name': 'Zed', 'age': 36, 'height': 74, 'city': 'Winston-Salem', 1: 'Wow'}

del stuff[1]
# {'name': 'Zed', 'age': 36, 'height': 74, 'city': 'Winston-Salem'}
print(stuff)

states = {
    "Oregon": "OR",
    'Florida': 'FL',
    'California': 'CA'
}

cities = {
    'CA': 'San Diego',
    'FL': 'Boca Raton',
    'OR': 'Bend'
}
cities['NY'] = 'New York'
cities['CA'] = 'LA'

# print some cities
print('-' * 10)
print('CA state has', cities['CA'])

# print some states
print('-' * 10)
print('Florida has: ', cities[states['Florida']])

# use state then cities dict
print('-' * 10)
print('Oregon has: ', cities[states['Oregon']])

# print ever state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print(f'{state} is abbreviated {abbrev}')

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print(f'{abbrev} has the city {city}')

# do both at same time
print('-' * 10)
for state, abbrev in states.items():
    print(f'{state} is abbreviated {abbrev} and has city {cities[abbrev]}')

print('-' * 10)
state = states.get('Texas', None)

if not state:
    print(f'Sorry, no Texas')

# get a city with a default value
city = cities.get('TX', "does not exist")
print(f'The city for the state "TX" is {city}')


###
# Dictionaries are good for looking up multiple values, look up tables
# Lists is for any sequence of things that need to go in order, and you only need to look them up by a numeric index
# What if you need a dict to be in order?
# -> collections.OrderedDict data structure in python
