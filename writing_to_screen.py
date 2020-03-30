#!/usr/bin/env python

actor = "Chris Hemsworth"
city = "Melbourne"

result = 29 / 8.23

print(actor)
print(result)
print(actor, result)
print()

print(actor, end="//")
print(result)

print(actor, result, sep="|")
print(actor, result, sep=", ")
print(actor, result, sep="")

print(result)

#       0             0
print("{:.3f}".format(result))

#      0          1          0      1
print("{} is from {}".format(actor, city))

print("{1} is from {0}".format(actor, city))

print(f"{actor} is from {city}")  # f-string

a = 29
b = 8.23
print(f"{a/b:.3f} {{good stuff}}")

print("%.3f" % (result))  # legacy formatting



