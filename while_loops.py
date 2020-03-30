#!/usr/bin/env python

i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    name = input("What is your name? (q to quit) ")
    if name == 'q':
        break
    if name == '':
        continue

    print("Welcome,", name)

#  & | ^ ~  and, or, xor, not for bits

