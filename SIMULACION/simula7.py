#!/usr/bin/python3
# -*-coding: utf-8 -*-
# Quinto ejercicio de Python con aleatorios, donde el ingreso
# de valores es a traves de consola para generar valores en
# un intervalo(a,b)
#
# Zhou Fucheng
# Feb/24/22
# al20760444.at.dot.edu.dot.mx
#
from operaciones import generar
import sys
import getopt
import argparse
import csv


class aleatorios:
    def __init__(self, datos):
        self.datos = datos
        self.cantidad = 15  # cantidad de aleatorios a generar por omision
        self.decimales = 2  # Numero de decimales por redondear, valor por omision
        try:
            opts, args = getopt.getopt(self.datos, "hv:V:n:d:", [
                                       "help", "vminima=", "vmaxima=", "cuantos=", "decimales="])
        except getopt.error:
            print('Modo de ejecutar el codigo: ')
            print(
                'simula6.py -v <valor_minimo> -V <valor_maximo> [-n cuantos] [-d decimales]')
            print('    ')
            print('escriba simula6,py --help para mayor información ')
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                parser = argparse.ArgumentParser(description='''
                El programa realiza una simulacion de numeros pseudoaletorios
                basandose en el metodo congruencial; los valores t asi como 
                del modulo ya se encuentran indicados dentro del codigo.
                El objetivo, es generar valores enteros comprendidos en el intervalo del
                (v,V) donde <v> representa al valor minimo y <V> al valor maximo.
                De manera adicional, el usuario podra determinar la cantidad de 
                de valores por generar, misma que se declara en la variable <n>
                asi entonces, esta cantidad debera ser un entero no negativo.
                ''', epilog='''
                En caso de no declarar ningun valor para <n>, se tomara como valor
                por default de construir 15 numeros pseudoaleatorios; asi mismo la variable
                <d> representa el numero de cifras decimales por redondear, de no señalarse,
                se tomaran dos cifras decimales.
                '''
                                                 )

                parser.add_argument(
                    '-v', '--vminima', help='Inicio del intervalo', type=float, required=True)
                parser.add_argument(
                    '-V', '--vmaxima', help='Fin del intervalo', type=float, required=True)
                parser.add_argument(
                    '-n', '--cuantos', help='Numero de peseudoaleatorios a ser generados', type=int, required=False)
                parser.add_argument(
                    '-d', '--decimales', help='Numero de cifras decimales por redondear', type=int, required=False)
                args = parser.parse_args()
            elif opt in ("-n", "--vminima"):
                try:
                    vminimo_temporal = float(arg)
                except:
                    print('No es posible generar la cantidad solicitada (1)')
                    sys.exit(2)
            elif opt in ("-V", "--vmaxima"):
                try:
                    vmamixo_temporal = float(arg)
                except:
                    print('No es posible generar la cantidad solicitada (2)')
                    sys.exit(2)
            elif opt in ("-n", "--cuantos"):
                try:
                    temporal_cantidad = int(arg)
                    if temporal_cantidad <= 0:
                        print('No es posible generar la cantidad solicitada(3)')
                        sys.exit(2)
                    self.cantidad = temporal_cantidad
                except:
                    print('No es posible generar la cantidad solicitada(4)')
                    sys.exit(2)
                try:
                    temporal_decimales = int(arg)
                    if temporal_cantidad <= 0:
                        print('No es posible generar la cantidad solicitada(5)')
                        sys.exit(2)
                    self.decimales = temporal_decimales
                except:
                    print('No es posible generar la cantidad solicitada')
                    sys.exit(2)
            aleatorios.simula(self)

        # Metodo para construir el intervalo de
        def simula(self):
            if self.vmaximo <= self.vminimo:
                print('No es posible realizar la simulacion')
                sys.exit(2)
            numeros_aleatorios = generar(self.cantidad)
            # Arreglo en donde se almacenaran los valores del intervalo
            valores = []
            for j in numeros_aleatorios:
                valores.append(round((self.vmaximo-self.vminimo)
                               * j+self.vminimo, self.decimales))
            self.solucion = valores

    def main():

        x = aleatorios(sys.argv[1:])
        data = []  # Arreglo donde estara la informacion que se manda a archivo
        header = ['Num', 'Calificacion']
        for i in range(len(x.solucion)):
            data.append([i+1, x.solucion[i]])
        with open('salida.csv', 'w', encoding='utf-8', newline='')as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
        print('El archivo ha sido generado')

    if __name__ == '__main__':
        main()
