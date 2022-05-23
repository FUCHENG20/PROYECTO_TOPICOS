#!/usr/bin/python3
#-*-coding: utf-8 -*-
#
# Generador de contraseñas seguras
#
# Zhou Fucheng
# Mar/01/22
# al20760444.at.ite.dot.edu.dot.mx
#

import sys, random

def realizar_contrasenia(cuantos):
    may=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V","W", "X", "Y", "Z"]
    minu=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z"]
    num=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    sig=["+", "-", ".", "-", "/", "*", "_"]
    contra=''
    for i in range(cuantos):
        opcion=random.randint(1,4)
        if opcion==1:
            valor=may[random.randint(0,len(may)-1)]
            contra=contra+valor
        elif opcion==2:
            valor=minu[random.randint(0,len(minu)-1)]
            contra=contra+valor
        elif opcion==3:
            valor=num[random.randint(0,len(num)-1)]
            contra=contra+valor
        elif opcion==4:
            valor=sig[random.randint(0,len(sig)-1)]
            contra=contra+valor
    return(contra)


def valorar(num_caracteres):
    if num_caracteres <=0:
        print("Intente con otro valor")
        sys.exit(2)
    else:
        contrasenia=realizar_contrasenia(num_caracteres)
        print(contrasenia)

def main():
    while True:
        try:
            n=int(input("Numeros de Caracteres para la contraseña: "))
            break
        except:
            print("Por favor, indique otro valor ")
    valorar(n)


if __name__ == '__main__':
    main()