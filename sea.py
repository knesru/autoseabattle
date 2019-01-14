from random import randint


class Cell:
    def __init__(self, x, y, content, sea=None):
        self.x = x
        self.y = y
        self.content = content
        self.sea = sea
        self.ship = None

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

    def boom(self) -> int:
        if self.content == self.sea.WATER:
            self.content = self.sea.MISS
        if self.content == self.sea.SHIP:
            self.content = self.sea.FIRE
        return self.content

    def str_sib(self):
        out = ''
        i = 1
        for c in self.get_siblings():
            if i % 3 == 0:
                out += '\n'
            if i == 5:
                out += ' '
            out += c.__str__()
            i += 1
        return out


class Ship:
    def __init__(self):
        self.cells = []

    def add_cell(self, cell: Cell):
        self.cells.append(cell)

    def is_sunk(self):
        for cell in self.cells:
            if cell.content == Sea.SHIP:
                return False
        return True


class Sea:
    WATER = 0
    SHIP = 1
    MISS = 2
    FIRE = 3

    RES_NONE = -1
    RES_MISS = 0
    RES_HIT = 1
    RES_SUNK = 2

    def __init__(self, width, height, is_visible):
        self.width = width
        self.height = height
        self.cells = []
        self.is_visible = is_visible
        for i in range(self.width):
            row = []
            for j in range(self.height):
                row.append(Cell(i, j, self.WATER, self))
                # row.append(Cell(i, j, randint(0, 4), self))
            self.cells.append(row)

    def get_cell(self, x, y) -> Cell:
        if x < 0 or x >= len(self.cells) or y < 0 or y >= len(self.cells[x]):
            raise IndexError('Out of sea!')
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

    def try_to_boom_cell(self, x, y) -> int:
        if x >= self.width or x < 0:
            return self.RES_NONE
        if y >= self.height or y < 0:
            return self.RES_NONE
        boom_result = self.get_cell(x, y).boom()
        if boom_result == self.FIRE:
            if self.get_cell(x, y).ship.is_sunk():
                return self.RES_SUNK
            return self.RES_HIT
        if boom_result == self.MISS:
            return self.RES_MISS

    def scan_cells(self):
        for i in range(self.width):
            for j in range(self.height):
                yield self.get_cell(i, j)
