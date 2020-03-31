#!/usr/bin/env python

person = "Bill", "Gates", "Microsoft", "1954-10-28"

print(person)
print(type(person))

print(person[0], person[1])

first_name, last_name, product, dob = person    # iterable unpacking....

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
]

print(type(people), type(people[0]), type(people[0][0]))
print(people[0])
print(people[0][0])
print(people[0][0][0])

for first_name, last_name, *product, dob in people:
    print(first_name, last_name, product)
print()

junk = [('Bob', 'MI'), ("Jane", "RI"), ("Peter", "VA")]

for person, state in junk:
    print(person, state)
print()

values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)
