#!/usr/bin/python3
#-*-coding: utf-8 -*-
#
# Se declaran las funciones auxiliares para los ejercicios
#
# Zhou Fucheng
# Feb/24/22
# al20760444.at.ite.dot.edu.dot.mx
#
from datetime import datetime
#Método que genera los números pseudo aleatorios
def generar(cantidad):
    t=4219 #Valor por omisión en caso de no ser declarado
    bandera=1 #Valor por omisión en caso de no ser declarado
    m=2**31-1 #Valor por omisión en caso de no ser declarado
    a=8*t+bandera*3
    ahora=datetime.now()
    semilla=ahora.microsecond
    # Se declara el arreglo inicial
    x=[]
    # Se declara el arreglo donde estarán los aleatorios
    y=[]
    # Se inicia el arreglo
    x.append(semilla)
    # Comienza el ciclo
    for i in range(cantidad+1):
        f=(a*x[i])%m
        x.append(f)
        if i > 0: #Se elimina la semilla del arreglo X para así obtener los aleatorios
            y.append(f/m)
    return y 

#Funcion que devolvera el dato de la tarjeta de Credito
def datos_tarjeta(semilla):
    t = 1233
    bandera = -1
    a = 8*t + bandera*3
    m = 2**16
    x = []
    x.append(semilla)
    for i in range(1,10):
        n = (a*x[i-1])%m
        x.append(n)
    for j in range (len(x)):
        #Convertir a Texto
        dato = str (x[j])
        #Se extraen los cuatros caracteres
        x[j] = dato[:4]
    return(x)