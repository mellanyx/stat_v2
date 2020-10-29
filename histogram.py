import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def histogram(data):
    """ Генеральная гистограмма """
    _data = []
    for el in data:
        _data.append(el)

    plt.hist(_data, histtype="stepfilled", edgecolor='#000100', linewidth=1.2)

    plt.title('Гистограмма')
    plt.ylabel('Частота')
    plt.xlabel('Данные')
    plt.grid(axis='y', alpha=0.75)

    plt.legend()
    plt.show()
