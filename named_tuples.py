#!/usr/bin/env python
from collections import namedtuple

Point = namedtuple('Point', 'x y')

p1 = Point(5, 9)
p2 = Point(8, 3)
p3 = Point(4, 7)

print(p1.x, p1.y)

Person = namedtuple('Person', 'first_name last_name product dob')

p = Person('Bill', 'Gates', 'Microsoft', '1954-10-28')
print(p.dob)
print(p[-1], p[0])

