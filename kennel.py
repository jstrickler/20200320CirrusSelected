#!/usr/bin/env python
from dog import Dog

d1 = Dog()    # Dog d1 = new Dog();
d2 = Dog()
d3 = Dog()

print(type(d1))

d1.bark()
d2.bark()
for i in range(5):
    d3.bark()
