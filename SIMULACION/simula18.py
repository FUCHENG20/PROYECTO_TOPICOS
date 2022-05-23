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

import sys
import csv
import random
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd


class Analisis():
    def __init__(self, root):
        self.root = root
        root.title("Calculo de Probabilidad")
        root.geometry("430x130")

        # Se la añade un Menu
        my_menu = Menu(root, bg="lightgrey", fg="black", tearoff=0)
        file_menu = Menu(my_menu)
        my_menu.add_cascade(label="Archivo", menu=file_menu)

        # file_menu.add_command(label="Obtener")
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=root.quit)
        action_menu = Menu(my_menu)
        my_menu.add_cascade(label="Acciones", menu=action_menu)

        # action_menu.add_command(label="Simular")
        root.configure(my_menu)

        # Solicitud de Informacion
        datos = Frame(root)
        datos.grid(column=0, row=0, padx=(50, 50), pady=(10, 10))
        self.forma = ttk.Combobox(datos, width=10, state='readonly')
        self.forma["values"] = ("Ecuacion", "Random", "Numpy")
        self.forma.grid(column=1, row=1)
        self.forma.current()

        # Opciones - ComboBox
        self.opciones = ttk.Combobox(datos, width=10, state='readonly')
        self.opciones["values"] = ("<", "<=", ">", ">=", "a<=x<=b")
        self.opciones.grid(column=1, row=1)
        self.opciones.current()

        # Mostramos la Solucion
        ttk.Label(datos, text="Solucion", justify=LEFT).grid(
            sticky=W, column=0, row=3)


def main():
    root = Tk()
    Analisis(root)
    root.mainloop()


if __name__ == '__main__':
    main()
