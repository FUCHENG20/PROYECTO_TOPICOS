#!/usr/bin/python
#
# Cuarto Ejercicio de Python con aleatorios
#
# By Zhou Fucheng
# Feb/15/2022
# al20760444.at.ite.dot.edu.dot.mx

t = 4219
bandera = 1
a = 8*t+bandera *3
semilla = 23456
m = 575629

# Se declara el Arreglo
x=[]
y=[]

# Se inicia el arreglo
x.append(semilla)

# Comienza el ciclo
for i in range (1,11):
	f = (a*x[i-1])%m
	x.append(f)

	#Condicion
	if (i >= 1):
		y.append(f/m)

for r in y:
	print('{:0.5f}'.format(r))