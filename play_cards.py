#!/usr/bin/env python

from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Joe", "PA")

print(d1)

print(d1.dealer)

d2 = CardDeck("Rhonda", 'CA')
print(d2.dealer)
print(d2.state)

def doit(deck: CardDeck):
    deck.whatever()

d1.whatever()
# same as
# CardDeck.whatever(d1)

d2.whatever()
# CardDeck.whatever(d2)

print(d1.get_dealer())
# print(d1.get_state())

d1.dealer = "Bob"

print(d1.dealer)

try:
    d1.dealer = 123.4
except TypeError as err:
    print(err)

d1.shuffle()
print(d1.cards)
print()

for _ in range(7):
    print(d1.draw())
print()

print(d1.cards)

print(d1.get_suits())

print(CardDeck.get_suits())

j1 = JokerDeck("Jill", "MO")
print(j1)
j1.shuffle()
for _ in range(5):
    print(j1.draw())
print()
print(j1.cards)
print()

j1.play()

print(JokerDeck.mro())

# print(len(d1.cards))
# print(len(j1.cards))

print(len(d1))
print(len(j1))

print(d1)
print(j1)

#  CardDeck(Betty, 43)
j2 = JokerDeck("Jimmy", "GA")
dd = d1 + j1 + d2 + j2
# dd  = (((d1 + j1) + d2) + j2)

print(dd)

print(repr(d1))

