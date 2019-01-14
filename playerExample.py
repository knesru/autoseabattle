import player
from sea import *


class Player(player.Player):
    # todo: Реализовывать обязательно. Это метод, который на основании предыдущего хода должен выдать тюлип координат для следующего
    def turn(self, prev_result):
        self.process_result(prev_result)
        if prev_result is None:
            return 3, 3
        if isinstance(prev_result, Cell):
            for cell in self.other_sea.scan_cells():
                if cell.content == Sea.WATER:
                    return cell.x, cell.y
            raise Exception('No more turns')

    def __init__(self, name='Example'):
        player.Player.__init__(self, name)

    # todo: Можно не реализовывать. =)) Базовое размещение вполне норм. ГЫ.
    # def place_ships(self):

    def process_result(self, result: Cell):
        if result is None:
            return
        try:
            self.other_sea.get_cell(result.x, result.y).content = result.content
        except IndexError:
            return
