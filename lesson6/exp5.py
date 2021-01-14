class Stationery:

    def __init__(self, title):
        self.tetle = title

    def drow(self):
        return 'Запуск отрисовки.'

class Pen(Stationery):
    def draw(self):
        return 'Запуск отрисовки {}'.format(self.tetle)

class Pencil(Stationery):
    def draw(self):
        return 'Запуск отрисовки {}'.format(self.tetle)

class Handle(Stationery):
    def draw(self):
        return 'Запуск отрисовки {}'.format(self.tetle)

pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашем')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())