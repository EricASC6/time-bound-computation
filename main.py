from Plotter import Plotter


def main():
    dir_path = "./data"
    plotter = Plotter(dir_path)
    plotter.read_csv()
    plotter.plot()


if __name__ == "__main__":
    main()
