class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polis = is_police

    def go(self):
        return 'The {} went.'.format(self.name)

    def stop(self):
        return '\nThe {} has stopped.'.format(self.name)

    def turn(self, direction):
        return '\nThe {} turned {}'.format(self.name, direction)

    def show_speed(self):
        return '\nYour speed is {}'.format(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'Превышение скорости. Твоя скорость {}.'.format(self.speed)
        else:
            return 'Машина {} едит.'.format(self.name)

class SportCar(Car):
    pass

class WorkCar(Car):
   def show_speed(self):
        if self.speed > 40:
            return 'Превышение скорости. Твоя скорость {}.'.format(self.speed)
        else:
            return 'Машина {} едит.'.format(self.name)

class PoliceCar(Car):
       pass

town = TownCar('BMW', 100, 'black', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('Formula 1', 300, 'white', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('KAMAZ', 35, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('MERSEDES', 100, 'blue', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())