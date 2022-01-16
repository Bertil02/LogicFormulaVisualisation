import data

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d

def histogramGraph(file):
    input_string, infoData = data.load(file)

    table = np.zeros((3,(int(infoData[0][2]))))
    for number in input_string:
        if (number == 0):
            continue
        elif (number > 0):
            table[0][number-1] = number
            table[1][number-1] += 1
        else:
            table[0][abs(number) - 1] = abs(number)
            table[2][abs(number) - 1] += 1

    print(table)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter(table[1],table[2],table[0])
    plt.xlabel("wystąpienia dodatnie")
    plt.ylabel("wystąpienia negacji")
    ax.set_zlabel("zmienna")
    plt.show()

histogramGraph('aim.cnf')
