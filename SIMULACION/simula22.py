#!/usr/bin/python
#
#
# Fucheng Zhou
# May/20/22
# al20760444.at.ite.dot.edu.dot.mx

from logging import root
import math
from re import L
import sys
from tkinter import messagebox
from scipy import stats
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
        root.title("Enfriamiento")
        root.geometry("450x400")

        # Se crea el frame para solicitar la informacion
        datos = Frame(root, height=2, bd=1, relief=SUNKEN)
        datos.pack(fill=X, padx=5, pady=5)

        # Valores del Intervalo a Graficar

        # Tiempo Inicial
        leyenda1 = ttk.Label(datos, text="Tiempo Inicial ", justify=LEFT)
        leyenda1.pack(fill=BOTH, expand=True)

        # Captura de la funcion
        self.TiempoInicial = Entry(datos, width=16)
        self.TiempoInicial.pack()

        # Temperatura Inicial
        leyenda2 = ttk.Label(datos, text="Temperatura Inicial ", justify=LEFT)
        leyenda2.pack(fill=BOTH, expand=True)

        # Captura de la funcion
        self.TemperaturaInicial = Entry(datos, width=16)
        self.TemperaturaInicial.pack()

        # Tiempo Final
        leyenda3 = ttk.Label(datos, text="Tiempo Final ", justify=LEFT)
        leyenda3.pack(fill=BOTH, expand=True)

        # Captura de la funcion
        self.TiempoFinal = Entry(datos, width=16)
        self.TiempoFinal.pack()

        # Temperatura Final
        leyenda4 = ttk.Label(datos, text="Temperatura Final ", justify=LEFT)
        leyenda4.pack(fill=BOTH, expand=True)

        # Captura de la funcion
        self.TemperaturaFinal = Entry(datos, width=16)
        self.TemperaturaFinal.pack()

        # Temperatura Medio Ambiente
        leyenda5 = ttk.Label(
            datos, text="Temperatura Medio Ambiente ", justify=LEFT)
        leyenda5.pack(fill=BOTH, expand=True)

        # Captura de la funcion
        self.TemperaturaMedioAmbiente = Entry(datos, width=16)
        self.TemperaturaMedioAmbiente.pack()

        # Frame de los Botones
        botones = Frame(root, height=2, bd=1, relief=SUNKEN)
        botones.pack(fill=X, padx=5, pady=5)
        ttk.Button(botones, text='Simular',
                   command=lambda: self.resolver()).grid(row=4, column=0)
        ttk.Button(botones, text='Salir',
                   command=root.quit).grid(row=4, column=1)

    # Parametros
    def parametro(self):
        x0 = int(self.TiempoInicial.get())
        y0 = float(self.TemperaturaInicial.get())
        x1 = int(self.TiempoFinal.get())
        y1 = float(self.TemperaturaFinal.get())
        x = []
        y = []
        x.append(x0)
        x.append(x1)
        y.append(math.log(y0))
        y.append(math.log(y1))
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        return(slope)

    # Funcion
    def funcion(self, x, y):
        k = self.parametro()
        TA = float(self.TemperaturaMedioAmbiente.get())
        return k*(y-TA)

    # Metodo Runge Kutta
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
        # Verificar Tiempo Inicial
        try:
            tiempo_inicial = int(self.TiempoInicial.get())
            if tiempo_inicial < 0:
                messagebox.showerror(
                    'Error', 'El Tiempo Inicial no puede ser Negativo')
                sys.exit(2)
        except ValueError:
            messagebox.showerror(
                'Error', 'Se debe de declarar el Tiempo Inicial')
            sys.exit(2)

        # Verificar Tiempo Final
        try:
            tiempo_final = int(self.TiempoFinal.get())
            if tiempo_final <= 0:
                messagebox.showerror(
                    'Error', 'El Tiempo Final no puede ser Negativo')
                sys.exit(2)
        except ValueError:
            messagebox.showerror(
                'Error', 'Se debe de declarar el Tiempo Final')
            sys.exit(2)

        # Verificar Temperatura Inicial
        try:
            temperatura_inicial = float(self.TemperaturaInicial.get())
            if temperatura_inicial <= 0:
                messagebox.showerror(
                    'Error', 'La Temperatura Inicial no puede ser Negativo')
                sys.exit(2)
        except ValueError:
            messagebox.showerror(
                'Error', 'Se debe de declarar la Temperatura Inicial')
            sys.exit(2)

        # Verificar Temperatura Final
        try:
            temperatura_final = float(self.TemperaturaFinal.get())
            if temperatura_final <= 0:
                messagebox.showerror(
                    'Error', 'La Temperatura Final no puede ser Negativo')
                sys.exit(2)
        except ValueError:
            messagebox.showerror(
                'Error', 'Se debe de Declarar la Temperatura Final')
            sys.exit(2)

        # Verificar Temperatura Medio Ambiente
        try:
            temperatura_medioambiente = float(
                self.TemperaturaMedioAmbiente.get())
            if temperatura_medioambiente < 0:
                messagebox.showerror(
                    'Error', 'La Temperatura del Medio Ambiente no puede ser Negativo')
                sys.exit(2)
        except ValueError:
            messagebox.showerror(
                'Error', 'Se debe de declarar la Temperatura del Medio Ambiente')
            sys.exit(2)

        # Primero, se crea la figua contenedora
        fig = Figure(figsize=(5, 5), dpi=100)
        # Se Llaman a los valores de RK
        vx, vy = self.rk4(self.funcion, tiempo_inicial,
                          temperatura_inicial, 50, 100)
        # Se crea una sub - figura
        plot1 = fig.add_subplot(111)
        # Se Grafica los Vectores
        plot1.plot(vx, vy)
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
