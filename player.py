import abc
from rules import Rules
from sea import *


class Player:
    def __init__(self):
        self.my_sea = Sea(Rules.width, Rules.height, True)
        self.other_sea = Sea(Rules.width, Rules.height, False)

    @abc.abstractmethod
    def turn(self, prev_result):
        #prev_result - object of class Cell or None
        pass

    def boom(self, x, y):
        return self.my_sea.try_to_boom_cell(x, y)
