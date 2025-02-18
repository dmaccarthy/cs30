# Copyright 2025 D.G. MacCarthy <https://github.com/dmaccarthy>
#
# This file is part of "sal_cs".
#
# "sal_cs" is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# "sal_cs" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "sal_cs".  If not, see <https://www.gnu.org/licenses/>.

from random import shuffle


class Card:
    "Class representing a single card from a standard 52-card deck"

    def __init__(self, card, suit):
        self._card = card, suit

    def __iter__(self):
        return iter(self._card)

    def __repr__(self):
        c, s = self._card
        return f"Card({c}, '{s}')"

    def __str__(self):
        c, s = self._card
        if c == 1:
            c = "Ace"
        elif c > 10:
            c = ["Jack", "Queen", "King"][c-11]
        return f"{c} of {s}"

    @property
    def suit(self):
        return self._card[1]

    @property
    def value(self):
        return self._card[0]


class Deck:
    "Class representing a standard 52-card deck of playing cards"

    def reset(self, shuf=True):
        self._cards = [Card(c, s) for s in ("Hearts", "Diamonds", "Spades", "Clubs") for c in range(1, 14)]
        if shuf: shuffle(self._cards)

    __init__ = reset

    def __len__(self): return len(self._cards)

    def shuffle(self): shuffle(self._cards)

    def draw(self, first=True):
        cards = self._cards
        if len(cards) == 0:
            raise IndexError("no cards remaining in deck")
        card = cards[0] if first else choice(cards)
        cards.remove(card)
        return card

    def deal(self, cards=5, first=True):
        return [self.draw(first) for i in range(cards)]
