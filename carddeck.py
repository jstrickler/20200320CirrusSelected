#!/usr/bin/env python
import random
# Java/C++/C#: this
# Python:      self

class CardDeck:   # inherits from 'object'
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer, state):
        self._state = None
        self._dealer = None
        self._cards = None
        #----
        self.dealer: str = dealer
        self.state: str = state
        self._make_deck()


    @property  # decorator
    def dealer(self):  # getter property
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def cards(self):
        return self._cards

    def get_dealer(self):
        return self._dealer

    # @property
    # def foom(self):
    #     return self._thing
    #
    # @foom.setter
    # def foom(self, value):
    #     self._thing = value

    # @property
    # def wombat(self):
    #     return self._wombat

    # def __new__(...): ....

    # private instance methods
    def _make_deck(self):
        self._cards = []   # list to hold cards
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = f"{rank}-{suit}"
                self._cards.append(card)

    # public instance methods

    # def cards_left(self):
    #     return len(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop(0)

    def whatever(self):
        print("T for Texas!")


    def __len__(self):
        return len(self.cards)

    def __str__(self):  # human-friendly
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}({self.dealer},{len(self)})"

    def __repr__(self):  # code-friendly
        my_type = type(self)
        my_name = my_type.__name__
        return f'{my_name}("{self.dealer}","{self.state}")'

    def __add__(self, other):
        tmp = type(self)(self.dealer, self.state)
        tmp._cards = self.cards + other.cards
        return tmp



    @classmethod
    def get_suits(cls):
        return cls.SUITS

    @staticmethod
    def doit():
        print("whooowhooooo")


if __name__ == '__main__':  # if running as primary script
    d = CardDeck("Angela", "NC")
    print(d)
    d.shuffle()
    print(d.cards)

# object data: part of self
# class data: part of class  (e.g., CardDeck)
