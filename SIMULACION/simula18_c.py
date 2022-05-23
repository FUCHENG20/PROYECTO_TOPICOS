#!/usr/bin/env python
# -*-coding: utf-8 -*-
#
# Metodo que emplea ventana grafico, donde el ususario
# selecciona el archivo csv correspondiente con la informacion
# a su vez el caluculo correspondiente
# para determinar una probabilidad dada
#
# Fucheng Zhou
# Mayo/3/22
# al20760444.at.ite.dot.edu.dot.mx

from argparse import FileType
from ast import Lambda
from codeop import CommandCompiler
from email.errors import MessageError
from multiprocessing.sharedctypes import Value
from re import L
import sys
import csv
import random
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from turtle import bgcolor


class Analisis():
    def __init__(self, root):

        self.root = root
        root.title("Calculo de Probabilidad")
        root.geometry("475x130")

        ###############################################################
        # MENU

        # Se la añade un Menu
        my_menu = Menu(root, bg="lightgrey", fg="black", tearoff=0)
        file_menu = Menu(my_menu)
        action_menu = Menu(my_menu)

        # Etiquetas para los elementos del Menu
        my_menu.add_cascade(label="Archivo", menu=file_menu)
        my_menu.add_cascade(label="Acciones", menu=action_menu)

        # Subelementos para Fila
        file_menu.add_command(
            label="Obtener", command=lambda: self.abrir_archivo())
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=root.quit)

        action_menu.add_command(label="Simular", command=lambda: self.simula())

        root.configure(menu=my_menu)

        ###############################################################
        # FRAMES

        # Solicitud de Informacion
        datos = Frame(root)
        # Solicitud de Valores
        sol = Frame(root)
        # Botones
        botones = Frame(root)

        radioboton = Frame(root)

        datos.grid(column=0, row=0, padx=(50, 50), pady=(10, 10))
        sol.grid(column=1, row=0, padx=(50, 50), pady=(10, 10))
        radioboton.grid(column=0, row=1, padx=(50, 50), pady=(10, 10))

        ################################################################
        # CAMPOS

        ttk.Label(datos, text="Tipo de Simulacion",
                  justify=LEFT).grid(sticky=W, column=1, row=1)
        ttk.Label(datos, text="Valor a Calcular",
                  justify=LEFT).grid(sticky=W, column=1, row=2)
        ttk.Label(datos, text="Solucion",
                  justify=LEFT).grid(sticky=W, column=1, row=3)

        ################################################################
        # ENTRADAS

        opcion = IntVar()
        self.forma = ttk.Radiobutton()
        ttk.Radiobutton(radioboton, text="Ecuacion", variable=opcion,
                        value=1).pack()

        ttk.Radiobutton(radioboton, text="Random", variable=opcion,
                        value=2).pack()
        ttk.Radiobutton(radioboton, text="Numpy", variable=opcion,
                        value=3).pack()

        # Tipo de Probabilidad
        self.opciones = ttk.Combobox(sol, width=10, state='randonly')
        self.opciones['value'] = ('<', '<=', '>', '>=', 'a<=x<=b')
        self.opciones.grid(column=1, row=2)
        self.opciones.current()

        # Valor de Calculo
        self.campoa = Entry(sol, width=6)
        self.campoa.grid(column=2, row=2)
        self.campob = Entry(sol, width=6)
        self.campob.grid(column=3, row=2)

        # Mostrar la Solucion
        self.solucion = Entry(sol, width=13)
        self.solucion.grid(column=1, row=3)

        ################################################################
        # BOTONES

        ttk.Button(botones, text='Simular',
                   command=lambda: self.simula()).grid(row=4, column=0)
        ttk.Button(botones, text='Salir',
                   command=root.quit).grid(row=4, column=1)

        ################################################################

        self.repeticiones = 30

    def abrir_archivo(self):
        datos = []

        # Solo se acepta CSV
        filetypes = [('Archivo CSV', '*.csv')]
        csv_path_file = fd.askopenfile(mode='r', filetypes=filetypes)
        if csv_path_file is not None:
            line_count = 0
            for row in csv_path_file:
                if line_count == 0:
                    line_count += 1
                else:
                    datos.append(float(row))
        else:
            pass
        self.data = datos

    def lectura1(self, combo1):
        switch = {
            'Ecuacion': 1,
            'Random': 2,
            'Numpy': 3
        }
        return switch.get(combo1, 'e')

    def lectura2(self, combo2):
        switch = {
            '<': 1,
            '<=': 2,
            '>': 3,
            '>=': 4,
            'a<=x<=b': 5
        }
        return switch.get(combo2, 'e')

    def valores_normales(self, opcion):
        # Aqui se almacenara la solucion
        valores = []
        promedio = np.average(self.data)
        desv = np.std(self.data)

        if opcion == 1:

            for i in range(self.repeticiones):
                suma = 0
                for i in range(12):
                    suma += random.random()
                    x = promedio + desv * (suma-6)
                    valores.append(x)

        elif opcion == 2:
            for i in range(self.repeticiones):
                valores.append(random.gauss(promedio, desv))

        else:
            valores = np.random.normal(promedio, desv, self.repeticiones)

        return(valores)

    def simula(self):

        # Validacion para el Campo a Calcular
        try:
            valor_inicial = float(self.campoa.get())
            if valor_inicial <= 0:
                messagebox.showerror(
                    'Error', 'El Valor a Determinar no Puede ser Negativo')
        except ValueError:
            messagebox.showerror(
                'Error', 'Debes de Indicar el Valor por Calcular')

        # Validacion para el combo de tipo de simulacion
        if not self.forma.get():
            messagebox.showerror('Error', 'Debe Indicar el Metodo a Simular')

        # Validacion para el combo de tipo por calcular
        if not self.opciones.get():
            messagebox.showerror('Error', 'Debe Indicar el Problema a Simular')

        metodo_simular = self.lectura1(self.forma.get())
        tipo_problema = self.lectura2(self.opciones.get())

        if(tipo_problema == 5):
            # Validacion para el campo a<=x<=b
            try:
                valor_final = float(self.campob.get())
                if (valor_final <= 0):
                    messagebox.showerror(
                        'Error', 'La Probabilidad Final no puede ser Negativa')
            except ValueError:
                messagebox.showerror('Error', 'Debe Declarar el Valor Final')
            if (valor_final <= valor_inicial):
                MessageError('Error', 'No es Posible Realizar el Calculo')

        # Valores de acuerdo a la distribucion normal
        valores = self.valores_normales(metodo_simular)
        suma = 0
        for j in valores:
            if tipo_problema == 1:
                if j < valor_inicial:
                    suma += 1
            elif tipo_problema == 2:
                if j <= valor_inicial:
                    suma += 1
            elif tipo_problema == 3:
                if j > valor_inicial:
                    suma += 1
            elif tipo_problema == 4:
                if j >= valor_inicial:
                    suma += 1
            else:
                if j <= valor_final and j >= valor_inicial:
                    suma += 1

        probabilidad = round((suma/self.repeticiones)*100, 2)
        self.solucion.delete(0, 'end')
        self.solucion.insert(0, probabilidad)


def main():
    root = Tk()
    Analisis(root)
    root.mainloop()


if __name__ == '__main__':
    main()
