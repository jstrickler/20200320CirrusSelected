#!/usr/bin/env python
import typing
import os

def get_message() -> str:
    return "Hello world"

def say_hello() -> None:
    m = get_message()
    print(m)

say_hello()

def decorate(s: str) -> str:
    i: int
    # i = "abc"
    return f"**{s.upper()}**"

print(decorate('spam'))

# print(decorate(123))

Numeric = typing.Union[int, float]


def doit(x: Numeric=1) -> float:
    return x * 10.0


def power(x=2, y=2):
    return x ** y


print(power(2, 5))

print(power(10), power(99), power(.5))

print(power(3, 5))

print(power(y=10))

def average(*values):
    if len(values) == 0:
        return 0.0
    total = sum(values)
    return total / len(values)

print(average(1, 100))
print(average(1, 5, 99, -2, 47))
print(average())

def spam(a, b, *c):
    print(a)
    print(b)
    print(c)

spam(1, 2)
spam(1, 2, 3, 4, 5, 6, 7)

def ham(**config):
    print(config)

ham(file_name='wombat.txt', country='Burkina Faso', number=5)

def wacky(p1, p2, *p3, p4, p5, **p6):
    pass




