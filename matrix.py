import time
from random import randint
from numba import jit
import numpy as np


@jit(nopython=True)
def multiply(m1, m2):
    product = []
    # loop through the rows in m1
    for i in range(len(m1)):
        row = []
        # loop through the columns in m2
        for j in range(len(m2[0])):
            val = 0
            # loop through the rows in m2 and get the vals in the same column
            for k in range(len(m2)):
                val += m1[i][k] * m2[k][j]

            row.append(val)
        product.append(row)
    return product


def generate_matrix(n, m):
    return np.random.rand(n, m)


def _time(func, m1, m2):
    figs = 1000000
    t1 = time.time()

    # invoke the func
    func(m1, m2)

    # get the time it took
    t2 = time.time()

    total = int((t2 - t1) * figs) / figs * 1000
    return total  # milliseconds
