#!/usr/bin/env python

actor = "Chris Hemsworth"

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"

print("Guido's the BDFL of Python")
print('Guido is the "BDFL" of Python')
print("Guido is the \"BDFL\" of Python")

print("""Guido's the "BDFL" of Python""")

print("spam\\n")

print(actor)
print(len(actor))   # NOT actor.len()

print(actor.upper())  # self-reference! in Java: 'this', in Python: 'self'

#  Foo x = Foo(123)
#  x.widget()
print(actor.upper(), actor.lower(), actor.capitalize(), actor.title())

print(actor.count('worth'), actor.count('h'), actor.count('chris'))
print(actor.count('Chris'))

#  print(myobj.len())  or print(myobj.length())
#  myobj.__len__(self)   same as len(myobj)

print(actor.lower().count('h'))

print(actor.find('worth'), actor.index('worth'))

print(actor.find('wombat'))

print(actor.find('h'))
print(actor.find('h', 8, 12))

print('wombat' in actor)
print('worth' in actor)

notes = 'tra la la'
print(notes.split())

data = 'Jane::Doe::Milwaukee::WI'
fields = data.split('::')
print(fields)

new_data = "//".join(fields)
print(new_data)

print(actor.replace('Chris', 'Liam'))

print(actor.replace('h', 'x'))
print(actor.lower().replace('h', 'X').title())

s = "     All my exes live in Texas     "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()


s = "xxyyxxxyyyAll my exes live in Texasxyxyxyyyyxxxyyxx"
print("|" + s.lstrip("xy") + "|")
print("|" + s.rstrip("xy") + "|")
print("|" + s.strip("xy") + "|")
print()

print(dir(s))
