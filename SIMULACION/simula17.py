#!/usr/bin/env python
# -*-coding: utf-8 -*-
#
# Ejercicio de Declaracion a traves del teclado (o shell)
#
# Fucheng Zhou
# Abril/26/22
# al20760444.at.ite.dot.edu.dot.mx

from importlib.machinery import WindowsRegistryFinder
import sys
import csv
import random
import time
from matplotlib import pyplot as plt
import numpy as np


class Aleatorios(object):
    def __init__(self, cantidad, **kwargs):
        self.media = 0
        self.desviacion = 1
        for key, value in kwargs.items():
            if float(value) <= 0:
                print('El valor de {} no puede ser negativo'.format(key))
                sys.exit(2)
            else:
                setattr(self, key, float(value))
        self.cantidad = cantidad


class Opciones(Aleatorios):

    """Clase para correr los metodos de eneracion de valores aleatorios de una distribucion normal"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    menu = """
    Bienvenido al Menu de Usuarios, seleccione la opcion del metodo de solucion
    que usted prefiera a continuacion seleccionando un numero del 1 al 4:
    [1] Ecuación correspondiente
    [2] Mediante la librería random
    [3] Mediante la librería numpy
    [4] Que realice los 3 anteriores al mismo tiempo
    """
    print(menu)

    def opcion1(self):
        inicio = time.perf_counter_ns()
        solucion1 = []
        for i in range(self.cantidad):
            suma = 0
            for j in range(12):
                suma += random.random()
            x = self.media + self.desviacion*(suma-6)
            solucion1.append(round(x, 2))
        fin = time.perf_counter_ns()
        tiempo_total_1 = fin-inicio
        return solucion1, tiempo_total_1

    def opcion2(self):
        inicio = time.perf_counter_ns()
        solucion2 = []
        for i in range(self.cantidad):
            x = round(random.gauss(self.media, self.desviacion), 2)
            solucion2.append(x)
        fin = time.perf_counter_ns()
        tiempo_total_2 = fin - inicio
        return solucion2, tiempo_total_2

    def opcion3(self):
        inicio = time.perf_counter_ns()
        solucion3 = []
        for i in range(self.cantidad):
            valor = np.random.rand()
            if valor <= 0.006:
                x = 20.78
            elif valor >= 0.007 and valor <= 0.067:
                x = 23.71
            elif valor >= 0.068 and valor <= 0.309:
                x = 26.64
            elif valor >= 0.31 and valor <= 0.692:
                x = 29.57
            elif valor >= 0.693 and valor <= 0.934:
                x = 32.5
            elif valor >= 0.935 and valor <= 0.995:
                x = 35.43
            else:
                x = 38.36
            solucion3.append(x)
        fin = time.perf_counter_ns()
        tiempo_total_3 = fin - inicio
        return solucion3, tiempo_total_3


def main(**kwargs):
    cantidad = 30
    x = Opciones(cantidad, **kwargs)
    valores1, tiempo1 = x.opcion1()
    valores2, tiempo2 = x.opcion2()
    valores3, tiempo3 = x.opcion3()

    print('=-='*11)
    opcion = input('Ingrese una opcion entre 1 y 4: \n')
    print('=-='*11)

    if opcion == '1':

        print("\nEl tiempo en realizar la opcion 1 fue {}" .format(
            tiempo1))
        data = []  # Arreglo donde estara la informacion que se manda a archivo
        header = ['No', 'Metodo-1']
        for i in range(cantidad):
            data.append([i+1, valores1[i]])
        with open('salida01.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
            data = valores1
            fig = plt.figure(figsize=(10, 7))
            # Creating plot
            plt.boxplot(data)
            # show plot
            plt.show()

    elif opcion == '2':

        print("\nEl tiempo en realizar la opcion 2 fue {}" .format(
            tiempo2))
        data = []  # Arreglo donde estara la informacion que se manda a archivo
        header = ['No', 'Metodo-2']
        for i in range(cantidad):
            data.append([i+1, valores2[i]])
        with open('salida02.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
            data = valores2
            fig = plt.figure(figsize=(10, 7))
            # Creating plot
            plt.boxplot(data)
            # show plot
            plt.show()

    elif opcion == '3':

        print("\nEl tiempo en realizar la opcion 3 fue {}" .format(
            tiempo3))
        data = []  # Arreglo donde estara la informacion que se manda a archivo
        header = ['No', 'Metodo-3']
        for i in range(cantidad):
            data.append([i+1, valores3[i]])
        with open('salida03.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
            data = valores3
            fig = plt.figure(figsize=(10, 7))
            # Creating plot
            plt.boxplot(data)
            # show plot
            plt.show()

    elif opcion == '4':

        print("\nEl tiempo en realizar la opcion1: {}, opcion 2: {} y opcion 3 fue {}" .format(
            tiempo1, tiempo2, tiempo3))
        data = []  # Arreglo donde estara la informacion que se manda a archivo
        header = ['No', 'Metodo-1', 'Metodo-2', 'Metodo-3']
        for i in range(cantidad):
            data.append([i+1, valores1[i], valores2[i], valores3[i]])
        with open('salida03.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
            data = valores1, valores2, valores3
            fig = plt.figure(figsize=(10, 7))
            # Creating plot
            plt.boxplot(data)
            # show plot
            plt.show()

    else:
        print('=-='*20)
        print('Debes ingresar un numero entre 1 y 4')
        print('=-='*20)


if __name__ == '__main__':
    main(**dict(arg.split('=') for arg in sys.argv[1:]))
