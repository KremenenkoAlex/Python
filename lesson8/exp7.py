class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b'

    def __add__(self, other):
        print(f'Сумма c_1 и c_2 равна')
        return f'c = {self.a + other.a} + {self.b + other.b}'

    def __mul__(self, other):
        print(f'Произведение c_1 и c_2 равно')
        return f'c = {self.a * other.a} * {(self.b * other.b)}'

    def __str__(self):
        return f'c = {self.a} + {self.b}'


c_1 = ComplexNumber(2, -3)
c_2 = ComplexNumber(4, 1)
print(c_1 + c_2)
print(c_1 * c_2)