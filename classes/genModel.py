import numpy as np
import collections
import math


class GenModel():

    def __init__(self, data):
        """ Генеральная совокупность """
        self.data = data

    def countEl(self, el):
        """ Возвращает количество вошедшего элемента """
        unique, counts = np.unique(self.sort(), return_counts=True)
        dict_count = dict(zip(unique, counts))

        return dict_count[el]

    def sort(self):
        """ Вариационный ряд """
        return np.sort(self.data)

    def mean(self):
        """ Среднее значение """
        N = len(self.data)
        result = 0
        for el in self.data:
            result += el

        return round(result / N, 2)

    def dispersion(self):
        """ Дисперсия """
        N = len(self.data)
        dispersion = 0
        for el in self.sort():
            dispersion += ((el - self.mean()) ** 2) * self.countEl(el)

        return round(dispersion / N, 2)

    def sigma(self):
        """ Сигма ген/выб """
        return round(math.sqrt(self.dispersion()), 2)

    def sample(self):
        return self.sort()[self.start::self.step]

    def revisedDispertion(self):
        """ Исправленная дисперсия выборки """
        return round(((len(self.data) / (len(self.data) - 1)) * self.dispersion()), 2)

    def revisedSigma(self):
        """ Исправленная сигма выборки 1 """
        return round(math.sqrt(self.revisedDispertion()), 2)
