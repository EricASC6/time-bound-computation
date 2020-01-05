import csv
import matplotlib.pyplot as plt
import os


class Plotter:
    def __init__(self, dir):
        self.dir = dir
        self.csv = []

    def read_csv(self):
        for fil in os.listdir(self.dir):
            path = os.path.join(self.dir, fil)
            with open(path, "r") as csv_file:
                csv_obj = csv.reader(csv_file)
                self.csv.append({
                    "name": os.path.splitext(fil)[0].capitalize(),
                    "csv": list(csv_obj)[1:]
                })

    def plot(self, _all=False):
        for csv_file in self.csv:
            input_size = [int(data[0])
                          for data in csv_file["csv"]]
            time = [float(data[1])
                    for data in csv_file["csv"]]
            plt.plot(input_size, time, label=csv_file["name"])
            plt.xlabel("Input Size")
            plt.ylabel("Time(ms)")
            plt.legend()
            if not _all:
                plt.title(csv_file["name"])
                plt.show()
        plt.title("All")
        plt.show()
