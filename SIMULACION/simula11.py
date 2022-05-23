#!/usr/bin/python3
#-*-coding: utf-8 -*-
#
# Validación de tarjetas de débito, empleando el algoritmo de construcción de números pseudo aleatorios.
#
# Zhou Fucheng
# Mar/01/22
# al20760444.at.ite.dot.edu.dot.mx
#

from cgitb import text
import math
import sys
from tkinter.tix import COLUMN
from operaciones import datos_tarjeta
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Tarjeta():
    def __init__(self,root):
        self.root=root
        root.title("Pago con tarjeta de crédito.")
        root.geometry("590x350")

        #####Texto del programa#####
        vtarjeta=Frame(root)
        vtarjeta.grid(column=0,row=0,padx=(50,50),pady=(10,10))
        ttk.Label(vtarjeta,text="Escriba su tarjeta de crédito", justify=LEFT).grid(sticky=W,column=0,row=0)

        #####Ingreso de valores#####
        datos_tarjeta=Frame(root)
        datos_tarjeta.grid(column=1,row=0,padx=(50,50),pady=(10,10))

        #####Campo 1#####
        self.campo1=Entry(datos_tarjeta,width=4)
        self.campo1.grid(column=0,row=0)

        #####Campo 2#####
        self.campo2=Entry(datos_tarjeta,width=4)
        self.campo2.grid(column=1,row=0)

        #####Campo 3#####
        self.campo3=Entry(datos_tarjeta,width=4)
        self.campo3.grid(column=2,row=0)

        #####Campo 4#####
        self.campo4=Entry(datos_tarjeta,width=4)
        self.campo4.grid(column=3,row=0)

        #####Campo de verificación#####
        ttk.Label(vtarjeta,text="Indique su código de verificación (CV)", justify=LEFT).grid(sticky=W,column=0,row=1)

        #####CV#####
        self.cv=Entry(datos_tarjeta,width=4)
        self.cv.grid(column=0,row=1)

        #####Fecha de Vencimiento ######
        vencimiento = Frame(root)
        vencimiento.grid(column=0, row=1, padx=(50,50), pady=(10,10))
        ttk.Label(vencimiento,text="Indique la fecha de vencimiento",
                  justify=LEFT).grid(sticky=W, column=0, row=0)
        
        #Datos para el Año
        ttk.Label(vencimiento, text="Año", justify=LEFT).grid(column=0, row=1)
        self.anio = Entry(vencimiento, width=4)
        self.anio.grid(column=1,row=1)
        
        #Datoss para el Mes
        ttk.Label(vencimiento, text="Mes").grid(column=2, row=1)
        opciones = ttk.Combobox(vencimiento, width=10, state="readonly")
        opciones["values"] = ("Enero", "Febrero", "Marzo", "Abril", "Mayo",
                              "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
                              "Diciembre")
        opciones.grid(column=3, row=1)
        opciones.current()
        
        
        #####Botón#####
        botones=Frame(root)
        botones.grid(column=0,row=2,padx=(50,50),pady=(10,10))
        ttk.Button(botones,text="Comprar", command=lambda:Tarjeta.verificar(self)).grid(row=4,column=0)
        ttk.Button(botones,text="Salir",command=root.quit).grid(row=4,column=1)

    def verificar(self):
        #Validacion Campo 1
        try:
            dato1=int(self.campo1.get())
            if dato1<=0:
                messagebox.showerror("Error, la lectura del primer campo es incorrecta")
                sys.exit(2)
            if dato1>=10000:
                messagebox.showerror("Error, la lectura del primer campo es incorrecta")
                sys.exit(2)
        except ValueError:
            messagebox.showerror("Error, se requiere de los 4 campos para continuar")
            sys.exit(2)

        #Validacion Campo 2
        try:
            dato2=int(self.campo2.get())
            if dato2<=0:
                messagebox.showerror("Error, la lectura del primer campo es incorrecta")
                sys.exit(2)
            if dato2>=10000:
                messagebox.showerror("Error, la lectura del primer campo es incorrecta")
                sys.exit(2)
        except ValueError:
            messagebox.showerror("Error, se requiere de los 4 campos para continuar")
            sys.exit(2) 

        #Validacion Campo 3
        try:
            dato3=int(self.campo3.get())
            if dato3<=0:
                messagebox.showerror("Error, la lectura del primer campo es incorrecta")
                sys.exit(2)
            if dato3>=10000:
                messagebox.showerror("Error, la lectura del primer campo es incorrecta")
                sys.exit(2)
        except ValueError:
            messagebox.showerror("Error, se requiere de los 4 campos para continuar")
            sys.exit(2)

        #Validacion Campo 4
        try:
            dato4=int(self.campo4.get())
            if dato4<=0:
                messagebox.showerror("Error, la lectura del primer campo es incorrecta")
                sys.exit(2)
            if dato4>=10000:
                messagebox.showerror("Error, la lectura del primer campo es incorrecta")
                sys.exit(2)
        except ValueError:
            messagebox.showerror("Error, se requiere de los 4 campos para continuar")
            sys.exit(2)   
        
        #Validacion Campo 1
        try:
            codigo_verificacion=int(self.cv.get())
            if codigo_verificacion<=0:
                messagebox.showerror("Error, el  Codigo de Verificacion es incorrecta")
                sys.exit(2)
            if codigo_verificacion>=10000:
                messagebox.showerror("Error, el codigo de Verificacion es incorrecta")
                sys.exit(2)
        except ValueError:
            messagebox.showerror("Error, se requiere de los 4 campos para continuar")
            sys.exit(2)

        ############################
        #AQUI COMIENZA LA SIMULACION
        ############################
        valores_tarjeta = datos_tarjeta(codigo_verificacion)
        #SEPARAR LOS VALORES DEL CODIGO DE VERIFICACION
        digito1 = math.floor(dato1/1000)
        digito2 = math.floor((dato1%1000)/100)
        digito3 = math.floor((dato1%100)/10)
        digito4 = math.floor((dato1%100)%10)
        #SE INICIALIZA EL CONTDOR
        contador = 0
        if valores_tarjeta[digito2] == self.campo2.get():
            contador += 1
        if valores_tarjeta[digito3] == self.campo3.get():
            contador += 1
        if valores_tarjeta[digito4] == self.campo4.get():
            contador += 1
        if contador == 3:
            messagebox.showinfo("Autorizada", "Su compra ha sido autorizada")
        else:
            messagebox.showerror("Rechazada", "Su compra no fue autorizada")
        
        
def main():
    root=Tk()
    Tarjeta(root)
    root.mainloop()

if __name__ == '__main__':
    main()