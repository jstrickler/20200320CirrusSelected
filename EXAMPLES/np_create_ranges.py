#!/usr/bin/env python
import numpy as np

r1 = np.arange(50)  # <1>
print(r1)
print("size is", r1.size)  # <2>
print()

r2 = np.arange(5, 101, 5)  # <3>
print(r2)
print("size is", r2.size)
print()

r3 = np.arange(1.0, 5.0, .3333333)  # <4>
print(r3)
print("size is", r3.size)
print()

r4 = np.linspace(1, 20, 100)  # <5>
print(r4)
print("size is", r4.size)
print()

r4.shape = 20, 5

r5 = np.round(r4, 2).transpose()
print(r5)

print(np.flip(r5))

