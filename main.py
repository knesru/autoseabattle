from random import randint


class Cell:
    def __init__(self, x, y, content, sea):
        self.x = x
        self.y = y
        self.content = content
        self.sea = sea

    def get_sib(self):
        siblings = (
            (-1, -1), (0, -1), (0, 1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1),
        )
        sibCells = []
        for displacement in siblings:
            sibCells = self.sea.getCell

    def __str__(self):
        types = [" ", "#", "•", "×"]
        if 0 > self.content or self.content >= len(types):
            return "?"
        return types[self.content]


class Sea:
    WATER = 0
    SHIP = 1
    MISS = 2
    FIRE = 3

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for i in range(self.width):
            row = []
            for j in range(self.height):
                # row.append(Cell(i, j, self.WATER, self))
                row.append(Cell(i, j, randint(0, 4), self))
            self.cells.append(row)

    def get_sell(self, x, y):
        return self.cells[x][y]

    def __str__(self):
        ret = "   "
        for i in range(self.width):
            ret += chr(ord("a")+i)+" "
        ret += "\n"
        for i in range(self.width):
            ret += str(i+1).rjust(2, ' ')+" "
            for j in range(self.height):
                ret += str(self.get_sell(j, i))+' '
            ret += "\n"
        return ret


sea = Sea(10, 10)

print(sea)
