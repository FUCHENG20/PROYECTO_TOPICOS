#!/usr/bin/env python
# -*-coding: utf-8 -*-
#
# Ejercicio de Declaracion a traves del teclado (o shell)
#
# Fucheng Zhou
# Abril/26/22
# al20760444.at.ite.dot.edu.dot.mx

import sys


class Aleatorios(object):
    def __init__(self, cantidad, **kwargs):
        self.media = 0
        self.desviacion = 1
        for key, value in kwargs.items():
            if float(value) <= 0:
                print('El valor de {} no puede ser negativo'.format(key))
                sys.exit(2)
            else:
                setattr(self, key, value)
        self.cantidad = cantidad


class Opciones(Aleatorios):
    """Clase para correr los metodos de eneracion de valores aleatorios de una distribucion normal"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def main(**kwargs):
    cantidad = 30
    x = Opciones(cantidad, **kwargs)
    print('La media es {} y la desviacion vale: {}' .format(x.media, x.desviacion))


if __name__ == '__main__':
    main(**dict(arg.split('=') for arg in sys.argv[1:]))
