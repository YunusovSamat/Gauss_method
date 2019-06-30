from fractions import Fraction

import numpy as np


class GaussMethod:
    def __init__(self, count_row, count_col, arr):
        self.n = count_row
        self.m = count_col
        self.x_vector = np.zeros(self.m-1, dtype="O")
        self.mtx = np.zeros((self.n, self.m), dtype="O")

        self.fill_matrix(arr)
        self.step_method()
        self.set_x_vector()

    def fill_matrix(self, arr):
        for i in range(self.n):
            self.mtx[i] = np.array(list(map(Fraction, arr[i])), dtype="O")

    def step_method(self):
        def conv_to_one(vector, k):
            if vector[k] == 0:
                print("Что-то пошло не так")
                exit(1)
            else:
                return vector / vector[k]

        def conv_to_zero(vector1, vector2, k):
            return vector1 * vector2[k] - vector2

        self.show_matrix()
        for i in range(self.n):
            if self.mtx[i][i] != 1:
                for row, elem in enumerate(self.mtx[i:, i]):
                    if abs(elem) == 1:
                        self.mtx[i], self.mtx[i + row] = (
                            self.mtx[i + row].copy() * elem,
                            self.mtx[i].copy()
                        )
                        self.show_matrix()
                        break
            self.mtx[i] = conv_to_one(self.mtx[i], i)
            for j in range(i + 1, n):
                self.mtx[j] = conv_to_zero(self.mtx[i], self.mtx[j], i)
            self.show_matrix()

    def set_x_vector(self):
        for i in range(self.n-1, -1, -1):
            for j in range(i+1, self.n):
                self.x_vector[i] -= self.mtx[i][j] * self.x_vector[j]
            self.x_vector[i] += self.mtx[i][-1]

        for i in range(self.m-1):
            self.x_vector[i] = float(self.x_vector[i])

    def show_matrix(self):
        for row in self.mtx:
            print("(", end="")
            for elem in row[:-1]:
                print("{0:^4}".format(str(elem)), end="")
            print("|{0:^4})".format(str(row[-1])))
        print()

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i > len(self.x_vector)-1:
            raise StopIteration
        else:
            value = self.x_vector[self.i]
            self.i += 1
            return value

    def __len__(self):
        return len(self.x_vector)

    def __str__(self):
        return str(self.x_vector)

    def iscorrentindex(self, i):
        if isinstance(i, (int, slice)):
            if isinstance(i, int) and (i > self.__len__()-1):
                raise IndexError
        else:
            raise TypeError

    def __getitem__(self, item):
        self.iscorrentindex(item)
        return self.x_vector[item]

    def __setitem__(self, item, value):
        self.iscorrentindex(item)
        self.x_vector[item] = value

    def __delitem__(self, item):
        self.iscorrentindex(item)
        del self.x_vector[item]

    def __contains__(self, value):
        return value in self.x_vector


if __name__ == '__main__':
    print("Введите кол-во строк: ", end="")
    while True:
        s = input()
        if s.isdigit():
            n = int(s)
            break
        else:
            print("Введенное значение не корректно.\n"
                  "Введите кол-во строк: ", end="")

    print("Введите данные матрицы:")
    array = []
    for i in range(n):
        while True:
            row_arr = input().split()
            if len(row_arr) == n+1:
                try:
                    array.append(list(map(float, row_arr)))
                except ValueError:
                    print("Введенное значение не корректно."
                          "\nВведите строку еще раз:")
                else:
                    break
            else:
                print("Количество столбцов не равно", n+1,
                      "\nВведите строку еще раз:")

    gm = GaussMethod(n, n+1, array)
    print(gm)
