import matrix
import csv
import numpy as np
import time


class DataGenerator:
    def __init__(self, high, interval, path, numpy=False):
        self.low = 0
        self.high = high
        self.interval = interval
        self.path = path
        self.numpy = numpy

    def generate_matrix(self, n, m):
        return matrix.generate_matrix(n, m)

    def get_performance(self, matrix_1, matrix_2):
        return matrix._time(matrix.multiply, matrix_1, matrix_2)

    def get_input_vs_time(self, i):
        matrix_1 = self.generate_matrix(i, i)
        matrix_2 = self.generate_matrix(i, i)
        time = self.get_performance(matrix_1, matrix_2)
        return [i, time]

    def generate(self):
        with open(self.path, "w") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Input", "Time"])
            if not self.numpy:
                for i in range(self.low, self.high + 1, self.interval):
                    print(i)
                    data = self.get_input_vs_time(i)
                    csv_writer.writerow(data)
            else:
                for i in range(self.low, self.high + 1, self.interval):
                    print(i)
                    matrix_1 = np.random.rand(i, i)
                    matrix_2 = np.random.rand(i, i)

                    figs = 1000000
                    t1 = time.time()
                    matrix_1.dot(matrix_2)
                    t2 = time.time()
                    total = int((t2 - t1) * figs) / figs * 1000
                    csv_writer.writerow([i, total])
