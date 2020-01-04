from DataGenerator import DataGenerator

normal_path = "./data/normal.csv"
high = 1000
interval = 10
min_val = -10
max_val = 10


normal_generator = DataGenerator(high, interval, min_val, max_val, normal_path)
normal_generator.generate()
