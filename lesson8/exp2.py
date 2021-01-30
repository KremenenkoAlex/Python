class division:
    def __init__(self, divisible, divider):
        self.divisible = divisible
        self.divider = divider

    @staticmethod
    def division_by_null(divisible, divider):
        try:
            return  (divisible / divider)
        except:
            return f"На ноль делить нельзя"

div = division(10, 100)
print(division.division_by_null(100, 0))
print(division.division_by_null(100, 10))
print(division.division_by_null(0, 10))
print(div.division_by_null(10, 100))