#!/usr/bin/python
#
#
# Fucheng Zhou
# May/13/22
# al20760444.at.ite.dot.edu.dot.mx

from logging import root
from re import L
from matplotlib.pyplot import plot
import numpy as np
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pyparsing import col


class Graficar():
    def __init__(self, root):
        self.root = root
        root.title("Graficador")
        root.geometry("450x400")
        # Se crea el frame para solicitar la informacion
        datos = Frame(root, height=2, bd=1, relief=SUNKEN)
        datos.pack(fill=X, padx=5, pady=5)
        leyenda1 = ttk.Label(datos, text="Funcion ", justify=LEFT)
        leyenda1.pack(fill=BOTH, expand=True)
        # Captura de la funcion
        self.funcion = Entry(datos, width=16)
        self.funcion.pack()
        # Valores del Intervalo a Graficar

        # Intervalo Inicial
        leyenda2 = ttk.Label(datos, text="Intervalo Inicial ", justify=LEFT)
        leyenda2.pack(fill=BOTH, expand=True)
        # Captura de la funcion
        self.campoa = Entry(datos, width=16)
        self.campoa.pack()

        # Intervalo Final
        leyenda3 = ttk.Label(datos, text="Intervalo Final ", justify=LEFT)
        leyenda3.pack(fill=BOTH, expand=True)
        # Captura de la funcion
        self.campob = Entry(datos, width=16)
        self.campob.pack()

        # Se crea el Frame de los Botones
        botones = Frame(root, height=2, bd=1, relief=SUNKEN)
        botones.pack(fill=X, padx=5, pady=5)
        ttk.Button(botones, text='Graficar',
                   command=lambda: self.plot()).grid(row=4, column=0)
        ttk.Button(botones, text='Salir',
                   command=root.quit).grid(row=4, column=1)

    def plot(self):
        # Primero, se crea la figua contenedora
        fig = Figure(figsize=(5, 5), dpi=100)
        # Se crea el Intervalo
        x = np.arange(float(self.campoa.get()), float(self.campob.get()))
        y = eval(self.funcion.get())
        # Se crea una sub - figura
        plot1 = fig.add_subplot(111)
        # Se Grafica
        plot1.plot(x, y)
        # Se anade a Tkinter como un elemento Canvas
        canvas = FigureCanvasTkAgg(fig, self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()


def main():
    root = Tk()
    Graficar(root)
    root.mainloop()


if __name__ == '__main__':
    main()
