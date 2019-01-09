from random import randint


class Cell:
    def __init__(self, x, y, content, sea):
        self.x = x
        self.y = y
        self.content = content
        self.sea = sea

    def get_siblings(self):
        siblings = (
            (-1, -1), (0, -1), (0, 1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1),
        )
        sib_cells = []
        for displacement in siblings:
            cell = self.get_neighbour(displacement)
            if cell:
                sib_cells.append(cell)
        return sib_cells

    def get_neighbour(self, displacement):
        newx = self.x + displacement[0]
        if newx < 0 or newx >= self.sea.width:
            return None
        newy = self.y + displacement[1]
        if newy < 0 or newy >= self.sea.height:
            return None
        return self.sea.get_cell(newx, newy)

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

    def get_cell(self, x, y):
        return self.cells[x][y]

    def __str__(self):
        ret = "   "
        for i in range(self.width):
            ret += chr(ord("a") + i) + " "
        ret += "\n"
        for i in range(self.width):
            ret += str(i + 1).rjust(2, ' ') + " "
            for j in range(self.height):
                ret += str(self.get_cell(j, i)) + ' '
            ret += "\n"
        return ret


sea = Sea(10, 10)

print(sea)
