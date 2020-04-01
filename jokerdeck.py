#!/usr/bin/env python
from carddeck import CardDeck

class Game:
    def play(self):
        print("playing...")


class JokerDeck(CardDeck, Game):

    def _make_deck(self):
        super()._make_deck()
        j1 = '1-Joker'
        j2 = '2-Joker'
        self._cards.append(j1)
        self._cards.append(j2)

