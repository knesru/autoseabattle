# from sea import *
#
# sea = Sea(10, 10)
# print(sea)
from sea import Sea, Cell
from playerExample import Player as P1
from playerFred import Player as P2
from random import randint

# todo: получать имя класса игроков из консольки
players = [P1('Example'), P2('Fred')]

for i in range(len(players)):
    players[i].place_ships()

# print(players[0])
# print(players[1])
results = [None, None]

current_player = randint(0, len(players) - 1)

while True:
    turn = players[current_player].turn(results[current_player])
    print('==================================')
    print(players[0])
    print(players[1])
    print(players[current_player].name, turn)
    result = players[(current_player + 1) % len(players)].boom(turn[0], turn[1])
    if result is not Sea.RES_NONE:
        if result > 0:
            results[current_player] = Cell(turn[0], turn[1], result)
        else:
            results[current_player] = Cell(turn[0], turn[1], result)
            current_player = (current_player + 1) % len(players)
    else:
        results[current_player] = Cell(turn[0], turn[1], None)

