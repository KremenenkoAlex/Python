from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def necessary(self):
        pass

class Coat(Clothes):
    def necessary(self):
        return "Сумма затраченной ткани на пальто равна: {:.2f}".format(self.param / 6.5 + 0.5)

class Suit(Clothes):
    def necessary(self):
        return "Сумма затраченной ткани на костюм равна: {:.2f}".format(2 * self.param + 0.3)

class Full(Clothes):
    @property
    def necessary(self):
        return "Сумма затраченной ткани равна: {:.2f}".format(self.param / 6.5 + 0.5 + 2 * self.param + 0.3)

coat = Coat(100)
suit = Suit(100)
full = Full(100)
print(coat.necessary())
print(suit.necessary())
print(full.necessary)