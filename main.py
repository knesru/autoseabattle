# from sea import *
#
# sea = Sea(10, 10)
# print(sea)
from sea import Sea, Cell
from playerManual import Player as P1
from playerExample import Player as P2
from random import randint

#todo: получать имя класса игроков из консольки
players = [P1(), P2()]

for i in range(len(players)):
    players[i].place_ships()

print(players[0].my_sea)
print(players[1].my_sea)
results = [None, None]

current_player = randint(0, len(players)-1)

while True:
    turn = players[current_player].turn(results[current_player])
    result = players[(current_player + 1) % len(players)].boom(turn[0], turn[1])
    if result is not Sea.RES_NONE:
        if result:
            results[current_player] = Cell(turn[0], turn[1], Sea.FIRE)
        else:
            results[current_player] = Cell(turn[0], turn[1], Sea.MISS)
            current_player = (current_player + 1) % len(players)
    else:
        results[current_player] = Cell(turn[0], turn[1], None)
    print('==================================')
    # print(players[0].my_sea)
    print(players[0].other_sea)
    print('-----------------------------------')
    # print(players[1].my_sea)
    print(players[1].other_sea)
