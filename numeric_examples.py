#!/usr/bin/env python

i1 = 100   # decimal integer
i2 = 0x100 # hex int
i3 = 0b100 # binary int
i4 = 0o100 # octal (not 0100 -- which is illegal)

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 0.

a = 23
b = 9

print(a + b)
print(a - b)
print(a * b)
print(a / b)   # true (float) division
print(a // b)  # floored (int) division
print(a ** b)  # raise a to power b
print(a % b)   # remainder of a // b
print(23 ** 23)

x = 10
x += 5  # x = x + 5
x *= 4
print(x)

# x++ ++x x-- --x  NOT IN Python

# x = 5
# y = x++
# z = ++x
# print(x, y, z)

#   P E M D A S

