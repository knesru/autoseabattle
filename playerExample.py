import player
from sea import *


class Player(player.Player):
    # todo: Реализовывать обязательно. Это метод, который на основании предыдущего хода должен выдать тюлип координат для следующего
    def turn(self, prev_result):
        if prev_result is None:
            return 3, 3
        if isinstance(prev_result, Cell):
            return prev_result.x + 1, prev_result.y + 1

    def __init__(self):
        player.Player.__init__(self)

    # todo: Можно не реализовывать. =)) Базовое размещение вполне норм. ГЫ.
    # def place_ships(self):
