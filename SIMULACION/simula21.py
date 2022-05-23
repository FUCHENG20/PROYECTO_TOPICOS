#!/usr/bin/python
#
# Problema del Paracaidista
#
# Fucheng Zhou
# May/19/22
# al20760444.at.ite.dot.edu.dot.mx

import sys
import numpy as np
import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt


class Graficar():
    def __init__(self, root):
        self.root = root
        root.title("Graficador")
        root.geometry("450x300")

        # Se crea el Frame para solicitarla información
        datos = Frame(root, height=2, bd=1, relief=SUNKEN)
        datos.pack(fill=X, padx=5, pady=5)
        leyenda1 = ttk.Label(datos, text="Velocidad del Avión", justify=LEFT)
        leyenda1.pack(fill=BOTH, expand=True)
        # leyenda1.pack()

        # Asignamos la Velocidad del avion
        self.VelocidadAvion = Entry(datos, width=16)
        self.VelocidadAvion.pack()

        # Asignamos la Velocidad del Viento
        leyenda2 = ttk.Label(datos, text="Velocidad del Viento", justify=LEFT)
        leyenda2.pack(fill=BOTH, expand=True)
        self.velocidadViento = Entry(datos, width=16)
        self.velocidadViento.pack()

        # Se crea el Frame para los botones
        botones = Frame(root, height=2, bd=1, relief=SUNKEN)
        botones.pack(fill=X, padx=5, pady=5)
        ttk.Button(botones, text="Graficar",
                   command=lambda: self.resolver()).grid(row=4, column=0)
        ttk.Button(botones, text="Salir",
                   command=root.quit).grid(row=4, column=1)

    def f(self, x, y):
        velocidad_viento = float(self.velocidadViento.get())
        # velocidad_avion = float(self.VelocidadAvion.get())
        A = 32/(velocidad_viento)
        B = math.sqrt(velocidad_viento)
        return A*(B-y)*(B+y)

    def rk4(self, f, x0, y0, x1, n):
        vx = [0] * (n + 1)
        vy = [0] * (n + 1)
        h = (x1 - x0) / float(n)
        vx[0] = x = x0
        vy[0] = y = y0
        for i in range(1, n + 1):
            k1 = h * f(x, y)
            k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
            k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
            k4 = h * f(x + h, y + k3)
            vx[i] = x = x0 + i * h
            vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
        return vx, vy

    def resolver(self):
        try:
            velocidad_avion = float(self.VelocidadAvion.get())
            if velocidad_avion <= 0:
                messagebox.showerror(
                    'Error', 'El avión no Puede llevar una velocidad Negativo')
                sys.exit(2)
        except ValueError:
            messagebox.showerror(
                'Error', 'Da la velocidad del avión')
            sys.exit(2)
        try:
            velocidad_viento = float(self.velocidadViento.get())
            if velocidad_viento <= 0:
                messagebox.showerror(
                    'Error', 'El viento no Puede llevar una velocidad Negativo')
                sys.exit(2)
        except ValueError:
            messagebox.showerror(
                'Error', 'Da la velocidad del viento')
            sys.exit(2)

        # Primero, se crea la figura contenedora

        # fig=Figure(figsize=(5,5), dpi=100)
        # Se crea el intervalo

        vx, vy = self.rk4(self.f, 0, velocidad_avion, 5, 100)
        plt.plot(vx, vy)
        plt.show()


def main():
    root = Tk()
    Graficar(root)
    root.mainloop()


if __name__ == '__main__':
    main()
