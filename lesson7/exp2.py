from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    def necessary(self):
        return "Сумма затраченной ткани равна: {:.2f}".format(self.param / 6.5 + 0.5 + 2 * self.param + 0.3)

    @abstractmethod
    def my_abstract(self):
        return "My abstractmethod 1 "

class Coat(Clothes):
    def necessary(self):
        return "Сумма затраченной ткани на пальто равна: {:.2f}".format(self.param / 6.5 + 0.5)

    def my_abstract(self):
        return "хрен знает как вывести общую длинну затраченной ткани"

class Suit(Clothes):
    def necessary(self):
        return "Сумма затраченной ткани на костюм равна: {:.2f}".format(2 * self.param + 0.3)

    def my_abstract(self):
        pass

coat = Coat(100)
suit = Suit(100)

print(coat.necessary())
print(suit.necessary())
print(coat.my_abstract())
print(suit.my_abstract())