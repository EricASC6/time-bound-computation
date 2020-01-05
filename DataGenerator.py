import matrix
import csv


class DataGenerator:
    def __init__(self, high, interval, min_val, max_val, path):
        self.low = 0
        self.high = high
        self.interval = interval
        self.min_val = min_val
        self.max_val = max_val
        self.path = path

    def generate_matrix(self, n, m):
        return matrix.generate_matrix(n, m, self.min_val, self.max_val)

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

            for i in range(self.low, self.high + 1, self.interval):
                print(i)
                data = self.get_input_vs_time(i)
                csv_writer.writerow(data)
