class Cell:
    def __init__(self, param):
        self.param = int(param)

    def __add__(self, other):
        return self.param + other.param

    # def __sub__(self, other):
        return self.param - other.param

    def __mul__(self, other):
        return self.param * other.param

    def __truediv__(self, other):
        return self.param // other.param

    def make_order(self, row):
        result = ''
        for i in range(int(self.param / row)):
            result += '*' * row + '\n'
        result += '*' * (self.param % row) + '\n'
        return result


cell_1 = Cell(50)
cell_2 = Cell(10)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(8))

