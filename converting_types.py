#!/usr/bin/env python

x = 123

m = "123"
n = 123.456

y = 'abc'

f = "DeadBeef"

print(str(x) + y)

print(hex(x), bin(x))

print(int(m), int(n))
print(int(y, 16), int(f, 16))

r = "foo"
s = "bar"
t = r + s
print(t)

w = "  123   "
print(int(w))

