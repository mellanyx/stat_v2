import collections
import classes
import numpy as np
import matplotlib.pyplot as plt


def poligon(data):
    """ Ген полигон """

    gen = classes.GenModel(data)

    list_x = []
    list_y = []

    for el in data:
        list_x.append((el + (el + 1)) / 2)
        list_y.append(gen.countEl(el))

    x = np.array(list_x)
    y = np.array(list_y)

    fig, ax = plt.subplots()
    #  Сплошная линия ('-' или 'solid',
    #  установлен по умолчанию):
    ax.plot(x, y,
            linestyle='-',
            linewidth=1,
            color='darkblue')

    fig.set_figwidth(12)
    fig.set_figheight(9)
    fig.set_facecolor('linen')
    ax.set_facecolor('ivory')

    plt.show()
