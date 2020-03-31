#!/usr/bin/env python

list1 = list()
cities = ['Austin', 'San Antonio', 'Fredericksburg']
list2 = []
list3 = "alpha beta gamma".split()
print(list3)

print(cities[0], cities[2])
print(cities[-1])
cities.append('Luckenback')
cities.append('New Braunfels')
print(cities, '\n')
cities.insert(0, "Round Rock")
cities.insert(3, "Dallas")
print(cities)

more_cities = ['Houston', 'Galveston', 'Brownsville', "Uvalde"]

cities.extend(more_cities)
print(cities)

del cities[7]
print(cities)

del more_cities

x = cities.pop()
print(x)
print(cities)

x = cities.pop(3)
print(x)
print(cities)

cities.remove('Galveston')
print(cities)

city = "Tulsa"
if city in cities:
    cities.remove(city)

cities[0] = "Dellville"

print(cities)

if city not in cities:
    print("awwww")

print(cities)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(fruits[0], fruits[1], fruits[2], fruits[-1], fruits[12])

print(fruits[0:5])   # fruit[0] through fruit[4]

print(fruits[3:8])

print(fruits[:5])
print(fruits[13:])
print(fruits[-5:])
print(fruits[::2])

actor = "Chris Hemsworth"
print(actor[:5], actor[10:])
print(actor[4:7], actor[6:9])
print()

#  S[start:stop:step]   start is INclusive stop is EXclusive

for city in cities:
    print(city)
print('-' * 60)

#  for VAR ... in ITERABLE:
#      # use VAR

for fruit in fruits:
    # fruit = next(fruits)
    print(fruit, end=' ')
print('\n')

print(fruit)

