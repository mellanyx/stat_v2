import classes
import numpy as np
from histogram import histogram
from poligon import poligon


def main():
    call = int(input('Введите номер задания: '))

    data = np.loadtxt("./X.txt", delimiter='\t', dtype=np.int)

    if (call == 1):
        gen = classes.GenModel(data)

        histogram(data)
        poligon(np.sort(data))
        writeInFileGen(call, data, gen.sort(), gen.mean(),
                       gen.dispersion(), gen.sigma())

    else:
        start = int(input('Введите с какого значения начать выборку: '))
        step = int(input('Введите шаг выборки: '))

        gen = classes.GenModel(np.sort(data[start::step]))

        histogram(np.sort(data))
        poligon(np.sort(data[start::step]))
        writeInFileSample(call, data[start::step], gen.sort(), gen.mean(), gen.dispersion(),
                          gen.revisedDispertion(), gen.sigma(), gen.revisedSigma())


def writeInFileGen(call, data, gen_sort, gen_mean,
                   gen_dispersion, gen_sigma):
    my_file = open(f"zad_{call}.txt", "w")
    my_file.write(f"""
    Часть №III
    Выборка из {len(data)} элементов
        
    {np.array(data)}

    1) Вариационный ряд из {len(gen_sort)} элементов

    {gen_sort}

    2) Среднее значение выборки = {gen_mean}

    Дисперсия выборки = {gen_dispersion}

    Сигма выборки = {gen_sigma}
    """)
    my_file.close()


def writeInFileSample(call, data, sample_sort, sample_mean, sample_dispersion,
                      sample_revised_dispersion, sample_sigma, sample_revised_sigma):
    my_file = open(f"zad_{call}.txt", "w")
    my_file.write(f"""
    Часть №III
    Выборка из {len(data)} элементов
        
    {np.array(data)}

    1) Вариационный ряд из {len(sample_sort)} элементов

    {sample_sort}

    2) Среднее значение выборки = {sample_mean}

    Дисперсия выборки = {sample_dispersion}

    Исправленная дисперсия выборки = {sample_revised_dispersion}

    Сигма выборки = {sample_sigma}

    Исправленная сигма выборки = {sample_revised_sigma}
    """)
    my_file.close()
