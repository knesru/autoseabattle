import player
from sea import *


class Player(player.Player):
    # todo: Реализовывать обязательно. Это метод, который на основании предыдущего хода должен выдать тюлип
    #  координат для следующего
    def turn(self, prev_result):
        self.process_result(prev_result)
        x = int(ord(input("X: ")) - ord('a') + 1)
        y = int(input("Y: "))
        return x, y

    def __init__(self):
        player.Player.__init__(self)

    # todo: Можно не реализовывать. =))
    #  Базовое размещение вполне норм. ГЫ.
    # def place_ships(self):

    def process_result(self, result: Cell):
        if result is None:
            return
        try:
            self.other_sea.get_cell(result.x, result.y).content = result.content
        except IndexError:
            pass
