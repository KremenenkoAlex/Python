class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:6}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(other.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix.__str__(self)

mat = Matrix([    [1, 0, 3], [0, 5, 0], [7, 0, 9], [0, 11, 0], [13, 0, 15]])
new_mat = Matrix([[0, 2, 0], [4, 0, 6], [0, 8, 0], [10, 0, 12], [0, 14, 0]])
print(mat.__add__(new_mat))