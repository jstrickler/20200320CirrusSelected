#!/usr/bin/env python

x = 100  # GLOBAL variable

def spam():
    y = 42  # LOCAL variable
    print("in spam(): x is", x)
    print(y)

spam()

# print("in main: y is", y)


