#!/usr/bin/env python
#
# Codigo con 4 Modificaciones Solicitadas
# 1.- Casillas tipo radio.
# 2.- Botones con estilo azul/blanco.
# 3.- Gráfica bigotes.
# 4.- Mostrar la media y desviación
#
# Fucheng Zhou
# Mayo/24/22
# al20760444.at.ite.dot.edu.dot.mx

from re import L
from statistics import mean
import sys
import random
import tkinter
from matplotlib import pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

class Analisis(ttk.Frame):
    def __init__(self, root):
        self.root = root
        root.title("Cálculo de Probabilidad")
        root.geometry("800x330")

       ###############################################################
       # MENU

        my_menu = Menu(root)

        # Se la añade un Menu
        file_menu = Menu(my_menu, tearoff=0)
        action_menu = Menu(my_menu, tearoff=0)

        # Elementos del Menu
        my_menu.add_cascade(label="Archivo", menu=file_menu)
        my_menu.add_cascade(label="Acciones", menu=action_menu)

        # Sub Elementos para file
        file_menu.add_command(
            label="Obtener", command=lambda: self.abrir_archivo())
        file_menu.add_separator()
        
        # Botones
        file_menu.add_command(label="Salir", command=root.quit)
        action_menu.add_command(label="Simular", command=lambda: self.simula())
        root.configure(menu=my_menu)


        ###############################################################
        # FRAMES

        # Label - Para Indicar que tipo de datos son
        info1 = Frame(root)  
        info2 = Frame(root)
        info3 = Frame(root)
        info4 = Frame(root)
        info1.grid(column=0, row=0, padx=(50), pady=(10))
        info2.grid(column=0, row=4, padx=(50), pady=(10))
        info3.grid(column=0, row=5, padx=(50), pady=(10))
        info4.grid(column=0, row=8, padx=(50), pady=(10))

        # Tipos de Botones
        botones = Frame(root)  
        radioboton = Frame(root)
        intervalos = Frame(root) 
        botones.grid(column=0, row=10, padx=(50), pady=(10))
        radioboton.grid(column=1, row=0, padx=(50), pady=(10))
        intervalos.grid(column=1, row=4, padx=(50), pady=(10))

        # Media y Desviacion
        media = Frame(root)
        desv = Frame(root)
        label = Frame(root)
        media.grid(column=0, row=2, padx=(50), pady=(10))
        desv.grid(column=1, row=2, padx=(50), pady=(10))
        label.grid(column=2, row=0, padx=(50), pady=(10))

        # Tipo de Solucion
        sol = Frame(root)
        sol.grid(column=1, row=5, padx=(50), pady=(10))

        # Solucion Final
        solucionf = Frame(root) 
        solucionf.grid(column=1, row=10, padx=(50), pady=(10))

        ################################################################
        # CAMPOS

        ttk.Label(info1, text="Tipo de Simulación :",
                  justify=LEFT).grid(sticky=W)
        ttk.Label(info2, text="Intervalos:", justify=LEFT).grid(
            sticky=W)
        ttk.Label(info3, text="Tipos de Intervalo: ", justify=LEFT).grid(
            sticky=W)
        ttk.Label(info4, text="Solución: ", justify=LEFT).grid(
            sticky=W)

        
        ################################################################
        # ENTRADAS

        # Tipo de Simulación
        self.opcion = IntVar()
        
        self.metodo1 = ttk.Radiobutton(radioboton, text="Ecuacion", variable=self.opcion, 
                    value=1).pack(side=LEFT)
        self.metodo2 = ttk.Radiobutton(radioboton, text="Random", variable=self.opcion,
                    value=2, ).pack(side=LEFT)
        self.metodo3 = ttk.Radiobutton(radioboton, text="Numpy", variable=self.opcion, 
                    value=3, ).pack(side=LEFT)
        
        # Opciones
        self.opciones = ttk.Combobox(
            sol, width=10, state="readonly")
        self.opciones["values"] = ("<", "<=", ">=", ">", "a<=x<=b")
        self.opciones.grid(column=0, row=1)
        self.opciones.current()
        self.repeticiones = 30

        # Valor de cálculo

        ttk.Label(intervalos, text="A: ",
                  justify=LEFT).pack(side=LEFT)
        self.campoA = Entry(intervalos,width=8)
        self.campoA.pack(side=LEFT)

        ttk.Label(intervalos, text="B: ",
                  justify=LEFT).pack(side=LEFT)
        self.campoB = Entry(intervalos, width=8)
        self.campoB.pack(side=RIGHT)


        # Campos de la Media y Desviacion
        ttk.Label(media, text="Media :",
                  justify=LEFT).pack(side=LEFT)
        self.media = Entry(media, width=10)
        self.media.pack()

        ttk.Label(desv, text="Desviacion :",
                  justify=LEFT).pack(side=LEFT)
        self.desv = Entry(desv, width=10)
        self.desv.pack()

        self.solucion = Entry(solucionf, width=20,state="readonly")
        self.solucion.pack()

        
        ################################################################
        # BOTONES
        
        self.simular = tkinter.Button(botones,
                                 text = "Simular",
                                 bg = "#227bd5",
                                 fg= "white",
                                 activeforeground="black",
                                 activebackground="white",
                                 relief="raised", borderwidth=3,
                                 width=20,
                                 cursor="hand1",
                                command=lambda: 
                                self.simula())

        self.simular.pack(side=LEFT, padx=0, pady=0)
        
        self.salir = tkinter.Button(botones,
                                 command=root.quit,
                                 text = "Salir",
                                 bg = "#227bd5",
                                 fg= "white",
                                 activeforeground="black",
                                 activebackground="white",
                                 relief="raised", borderwidth=3,
                                 width=15,
                                 cursor="hand1"
                                 )

        self.salir.pack(side=RIGHT, padx=15, pady=20)
        self.root.mainloop()


    def abrir_archivo(self):
        self.datos = []
        
        # Solo se Permiten archivos .csv
        filetypes = [("Archivo CSV", "*.csv")]
        csv_path_file = fd.askopenfile(mode="r", filetypes=filetypes)
        if csv_path_file is not None:
            line_count = 0
            for row in csv_path_file:
                if line_count == 0:
                    line_count += 1
                else:
                    self.datos.append(float(row))
                    self.st_dev = np.std(self.datos)
        else:
            pass
        self.data = self.datos
        
        self.media.insert(0, round(mean(self.datos),5))
        self.desv.insert(0, round(float(str(self.st_dev)),6))
        
    
    def tiposimulacion(self, combo1):
        switch = {"Ecuacion": 1, "Random": 2, "Numpy": 3}
        return switch.get(combo1, "e")
    
    def tipointervalo(self, combo2):
        switch = {"<": 1, "<=": 2, ">=": 3, ">": 4, "a<=x<=b": 5}
        return switch.get(combo2, "e")
       
    def valores_normales(self, opcion):
        valores = []
        try:
            promedio = float(self.media.get())
        except:
            promedio = np.average(self.data)

        try:
            desv = float(self.desv.get())
        except:
            desv = np.average(self.data)
        
        if opcion == 1:
            for i in range(self.repeticiones):
                suma = 0
                for j in range(12):
                    suma += random.random()
                x = promedio + desv * (suma-6)
                valores.append(x)
        elif opcion ==2:
            for i in range(self.repeticiones):
                valores.append(random.gauss(promedio, desv))
        else:
            valores = np.random.normal(promedio, desv, self.repeticiones)

        return (valores)


    def simula(self):
        
        # Validación para el combo de tipo de simulación
        if not self.opcion.get():
            messagebox.showerror(
                "Error", "No se seleccionó un tipo de simulación.")
            sys.exit(2)

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


        metodo_simular = self.tiposimulacion(self.opcion.get())
        tipo_problema = self.tipointervalo(self.opciones.get())

        if tipo_problema==5:
            #validacion para el campo a<x<b
            try:
                valor_final = float(self.campoB.get())
                if valor_final <= 0:
                    messagebox.showerror("Error", "La probabilidad final no puede")
                    sys.exit(2)
            except ValueError:
                messagebox.showerror("Error", "Debe declarar el valor final")
                sys.exit(2)
            if valor_final <= valor_inicial:
                messagebox.showerror("Error", "No es posible realizar el calculo")
                sys.exit(2)
        
        #Valores de acuerdo a la distribucion normal
        valores = self.valores_normales(metodo_simular)
        suma = 0
        for j in valores:
            if tipo_problema ==1:
                if j < valor_inicial:
                    suma +=1
            elif tipo_problema ==2:
                if j <= valor_inicial:
                    suma +=1
            elif tipo_problema ==3:
                if j > valor_inicial:
                    suma +=1
            elif tipo_problema ==4:
                if j >= valor_inicial:
                    suma +=1
            else:
                if j <= valor_final and j >= valor_inicial:
                    suma +=1
        
        probabilidad = round((suma/self.repeticiones)*100,2)
        
        re = StringVar()
        re.set(str(probabilidad))
        self.solucion.config(textvariable=re)
        var = []
        var = self.datos, valores
        fig = plt.figure(figsize =(10, 7))

        # Creating plot
        plt.boxplot(var)
        # show plot
        plt.show()
        
        

        

def main():
    root = Tk()
    Analisis(root)
    root.mainloop()
    


if __name__ == '__main__':
    main()

