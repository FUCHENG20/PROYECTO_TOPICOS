#!/usr/bin/python
#
# Método que emplea ventana gráfica, donde el usuario
# selecciona el archivo CSV correspondiente con la información,
# a su vez, el cáculo correspondiente para determinar una
# probabilidad dada.
#
# Fucheng Zhou
# May/03/22
# al20760444.at.ite.dot.edu.dot.mx
#
from ast import Lambda
import re
import sys
import random
from turtle import bgcolor
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd


from pyparsing import col, line_end


class Analisis():
    def __init__(self, root):
        self.root = root
        root.title("Cálculo de Probabilidad")
        root.geometry("450x430")

        #Menú#
        ################################################################
        my_menu = Menu(root, bg="lightgrey", fg="black")

        # Elementos que contendrá el menú
        file_menu = Menu(my_menu, tearoff=0)
        action_menu = Menu(my_menu, tearoff=0)

        # Etiquetas para los elementos del menú
        my_menu.add_cascade(label="Archivo", menu=file_menu)
        my_menu.add_cascade(label="Acciones", menu=action_menu)

        # Subelementos para file
        file_menu.add_command(
            label="Obtener", command=lambda: self.abrir_archivo())
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=root.quit)

        # Subelementos para action
        action_menu.add_command(label="Simular", command=lambda: self.simula())

        # Se crea el elemento (se compagina)
        root.configure(menu=my_menu)

        #Frames#
        ################################################################
        datos1 = Frame(root)
        # Solicitud de información
        datos2 = Frame(root)
        # Solicitud de información
        datos3 = Frame(root)
        # Solicitud de información
        sol = Frame(root)
        # Solicitud de valores
        botonFunciones = Frame(root)
        # Botones
        radiobutton = Frame(root)
        # Botones
        botuns = Frame(root)
        # Botones
        datos1.grid(column=0, row=0, padx=(50), pady=(10))
        datos2.grid(column=0, row=2, padx=(50), pady=(10))
        datos3.grid(column=0, row=4, padx=(50), pady=(10))
        sol.grid(column=0, row=3, padx=(50), pady=(10))
        radiobutton.grid(column=0, row=1, padx=(50), pady=(10))
        botuns.grid(column=1, row=3, padx=(50), pady=(10))
        botonFunciones.grid(column=0, row=5, padx=(50), pady=(10))

        #Campos#
        ################################################################
        ttk.Label(datos1, text="Tipo de simulación.",
                  justify=LEFT).grid(sticky=W, column=1, row=1)
        ttk.Label(datos2, text="Valor a calcular:", justify=LEFT).grid(
            sticky=W, column=1, row=2)
        ttk.Label(datos3, text="Solución", justify=LEFT).grid(
            sticky=W, column=1, row=3)

        #Entradas#
        ################################################################
        # Tipo de simulación

        opcion = IntVar()
        self.forma = ttk.Radiobutton()
        ttk.Radiobutton(radiobutton, text="Ecuacion", variable=opcion,
                        value=1).pack()

        ttk.Radiobutton(radiobutton, text="Random", variable=opcion,
                        value=2).pack()
        ttk.Radiobutton(radiobutton, text="Numpy", variable=opcion,
                        value=3).pack()

        print(ttk.Combobox)
        # Tipo de probabilidad
        #self.opciones = ttk.Combobox(sol, width=10, state="readonly")
        #self.opciones["values"] = ("<", "<=", ">=", ">", "a<=x<=b")
        #self.opciones.grid(column=0, row=1)
        # self.opciones.current()

        # Valor de cálculo
        self.campoA = Entry(botuns, width=6)
        self.campoA.pack()
        self.campoB = Entry(botuns, width=6)
        self.campoB.pack()

        # Mostrar la solución
        self.solucion = Entry(botonFunciones, width=13, state="readonly")
        self.solucion.pack()

        #Botones#
        ################################################################

        self.buttonA = ttk.Button(botonFunciones,
                                  text="Simular",
                                  bg="blue",
                                  fg="white",
                                  command=lambda:
                                  self.simula())

        self.buttonA.pack(side=LEFT, padx=0, pady=0)

        self.buttonB = ttk.Button(botonFunciones,
                                  text="Salir",
                                  bg="blue",
                                  fg="white")

        self.buttonB.pack(side=RIGHT, padx=15, pady=20)
        self.root.mainloop()

        #Botones#
        ################################################################
        self.repeticiones = 30

    def abrir_archivo(self):
        datos1 = []
        datos2 = []
        datos3 = []
        # Solo se aceptan archivos .csv
        filetypes = [("Archivo CSV", "*.csv")]
        csv_path_file = fd.askopenfile(mode="r", filetypes=filetypes)
        if csv_path_file is not None:
            line_count = 0
            for row in csv_path_file:
                if line_count == 0:
                    line_count += 1
                else:
                    datos1.append(float(row))
                    datos2.append(float(row))
                    datos3.append(float(row))

        else:
            pass
        self.data = datos1
        self.data = datos2
        self.data = datos3

    def lectura2(self, combo2):
        switch = {"<": 1, "<=": 2, ">=": 3, ">": 4, "a<=x<=b": 5}
        return switch.get(combo2, "e")

    def simula(self):
        # Validación para el combo de tipo de simulación
        #######arreglar###############
       # if  self.forma.pack() :
       #     messagebox.showerror(
       #         "Error", "No se seleccionó un tipo de simulación.")
       #     sys.exit(2)

        # Validación para el combo de tipo de problema para calcular
        if not self.opciones.get():
            messagebox.showerror(
                "Error", "No se seleccionó un tipo de problema.")
            sys.exit(2)

        # Validez para el campo a calcular
        try:
            valor_inicial = float(self.campoA.get())
            if valor_inicial <= 0:
                messagebox.showerror(
                    "Error", "Los valores no pueden ser negativos")
                sys.exit(2)
        except ValueError:
            messagebox.showerror(
                "Error", "Debe indicar los valores por calcular")
            sys.exit(2)
        tipo_problema = self.lectura2(self.opciones.get())


def main():
    root = Tk()
    Analisis(root)
    root.mainloop()


if __name__ == '__main__':
    main()
