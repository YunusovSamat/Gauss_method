from fractions import Fraction

import numpy as np


class GaussMethod:
    def __init__(self, count_row, count_col, arr):
        self.n = count_row
        self.m = count_col
        self.mtx = np.zeros((n, m), dtype="O")

        self.fill_matrix(arr)
        self.step_method()

    def fill_matrix(self, arr):
        for i in range(n):
            self.mtx[i] = np.array(list(map(Fraction, arr[i])), dtype="O")

    def step_method(self):
        def conv_to_one(vector, k):
            return vector / vector[k]

        def conv_to_zero(vector1, vector2, k):
            return vector1 * vector2[k] - vector2

        print(self)
        for i in range(n):
            if self.mtx[i][i] != 1:
                for row, elem in enumerate(self.mtx[i:, i]):
                    if abs(elem) == 1:
                        self.mtx[i], self.mtx[i + row] = (
                            self.mtx[i + row].copy() * elem,
                            self.mtx[i].copy()
                        )
                        print(self)
                        break
            self.mtx[i] = conv_to_one(self.mtx[i], i)
            for j in range(i + 1, n):
                self.mtx[j] = conv_to_zero(self.mtx[i], self.mtx[j], i)
            print(self)

    def __str__(self):
        show = ""
        for row in self.mtx:
            show += "("
            for elem in row[:-1]:
                show += "{0:^4}".format(str(elem))
            show += "|{0:^4})\n".format(str(row[-1]))
        return show


if __name__ == '__main__':
    # n = int(input("Введите кол-во строк: "))
    n = 4
    m = n + 1

    # t = [
    #     [3, 2, -5, -1],
    #     [1, 2, -1, 9],
    #     [2, -1, 3, 13]
    # ]

    t2 = [
        [2, 5, 4, 1, 20],
        [1, 3, 2, 1, 11],
        [2, 10, 9, 7, 40],
        [3, 8, 9, 2, 37]
    ]

    # print("Введите данные матрицы:")
    # for i in range(n):
    #     row_arr = input().split()
    #     mtx[i] = list(map(int, row_arr))

    gm = GaussMethod(n, m, t2)

