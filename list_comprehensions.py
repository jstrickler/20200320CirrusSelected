#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

#    [ expr     for VAR in ITERABLE if CONDITION]
f1 = [f.upper() for f in fruits]  # list comprehension
print("f1:", f1, '\n')
f1 = (f.upper() for f in fruits)  # generator expression


f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

things = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs',
    'spam', 'spam', 'toast', 'bacon', 'pancakes','spam', 'spam',
          'spam', 'spam', 'spam', 'spam']

breakfast = [t for t in things if t != 'spam']
print("breakfast:", breakfast, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = []
for p in people:
    last_names.append(p[1])

last_names = [p[1] for p in people]
print("last names:", last_names, '\n')

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = [10 * float(n) for n in nums if n > 100]
print("n1:", n1, '\n')

n2 = (float(n) for n in nums)
print(n2)
for value in n2:
    print(value)
print()

other_nums = [5, 8, 6, 4, 7, 5, 14, 2]

n3 = (i * j for i in nums for j in other_nums)
print(n3)
print(list(n3))

n4 = (i * j for i, j in zip(nums, other_nums))
print(n4)
print(list(n4))

a = ['a', 'b', 'c', 'd', 'e']
b = [1, 2, 3]

x = zip(a, b)
print(x)
print(list(x))

