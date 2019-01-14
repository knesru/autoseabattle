import abc
from rules import Rules
from sea import *


class Player:
    def __init__(self, name='player'):
        self.name = name
        self.my_sea = Sea(Rules.width, Rules.height, True)
        self.other_sea = Sea(Rules.width, Rules.height, False)
        self.ships = Rules.ships

    @abc.abstractmethod
    def turn(self, prev_result):
        # prev_result - object of class Cell or None
        pass

    def boom(self, x, y):
        return self.my_sea.try_to_boom_cell(x, y)

    def place_ship(self, length, x, y, horizontal=True):
        if length < 0 or length >= len(self.ships):
            return False
        for i in range(length):
            if self.my_sea.get_cell(x, y) is None or self.my_sea.get_cell(x, y).content != Sea.WATER:
                return False
            for cell in self.my_sea.get_cell(x, y).get_siblings():
                if cell.content in (Sea.FIRE, Sea.SHIP):
                    return False
            if horizontal:
                x += 1
            else:
                y += 1
        if horizontal:
            x -= length
        else:
            y -= length
        ship = Ship()
        for i in range(length):
            self.my_sea.get_cell(x, y).content = Sea.SHIP
            self.my_sea.get_cell(x, y).ship = ship
            ship.add_cell(self.my_sea.get_cell(x, y))
            if horizontal:
                x += 1
            else:
                y += 1
        self.ships[length] -= 1
        return True

    def place_ships(self):
        self.place_ship(4, 1, 1)
        self.place_ship(3, 6, 1)
        self.place_ship(3, 1, 3)
        self.place_ship(2, 5, 3)
        self.place_ship(2, 8, 3)
        self.place_ship(1, 1, 5)
        self.place_ship(1, 3, 5)
        self.place_ship(1, 5, 5)
        self.place_ship(1, 7, 5)

    def __str__(self):
        my_sea_arr = self.my_sea.__str__().split('\n')
        other_sea_arr = self.other_sea.__str__().split('\n')
        res = 'Name:'+self.name+'\n'
        for row in range(len(my_sea_arr)):
            res += my_sea_arr[row] + '\t|\t' + other_sea_arr[row] + '\n'
        return res
