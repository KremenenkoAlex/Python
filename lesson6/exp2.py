class Road:

    def __init__(self, length:int, width:int):
        self._lenght = length
        self._width = width
        self.weight = 30
        self.height = 10

    def weight_asphalt(self):
        weight_asphalt = self._lenght * self._width * self.weight * self.height / 1000
        print('Для покрытия дорожного полотна неободимо {} т. массы асфальта'.format(round(weight_asphalt)))

road = Road(10000, 20)
road.weight_asphalt()
