#!/usr/bin/python
#
# Primer Ejercicio de Python con aleatorios
#
# By Zhou Fucheng
# Feb/11/2022
# al20760444.at.ite.dot.edu.dot.mx

a = 1576
b = 789
semilla = 23456
m = 575629

# Se declara el Arreglo
x=[]
x.append(semilla)

# Se crea el ciclio
for i in range(1,11):
	l=(a*x[i-1]+b)%m
	x.append(l)

for j in range (len(x)):
	x[j]=x[j]/m

for l in x:
	print('{:0.5f}'.format(l))