#!/usr/bin/python3
#-*-coding: utf-8 -*-
#
# Ejercicio de Python con aleatorios, para estimar un ingreso promedio
#
# Zhou Fucheng
# Feb/25/22
# al20760444.at.ite.dot.edu.dot.mx
#
from operaciones import generar
import sys,getopt,argparse,csv
class aleatorios:
    def __init__(self,datos):
        self.datos=datos
        self.precio_venta=60 #Precio de venta por default
        self.dias=30 #Número de días a simular por omisión
        self.decimales=2 #Numero de decimales por redondear, valor por omisión
        try:
            opts,args=getopt.getopt(self.datos,"hv:V:p:d:",["help","vminima=","vmaxima=","precio=","dias="])
        except getopt.error:
            print('Modo de ejecutar el código: ')
            print('simula8.py -v <venta_minima> -V <venta_maxima> [-p precio] [-d dias] ')
            print(' ')
            print('escriba simula8.py --help para mayor información ')
            sys.exit(2)
        for opt,arg in opts:
            if opt in ("-h","--help"):
                parser=argparse.ArgumentParser(description='''
                    El objetivo, es generar un archivo en donde se calcula el ingreso 
                    de acuerdo a las ventas en el intervalo (v,V) donde <v> representa la
                    venta mínima y <V> la venta máxima.
                    El usuario podrá determinar la cantidad de días por simular, misma que 
                    se declara en la variable <d>; así entonces, esta cantidad deberá ser un 
                    entero no negativo.
                    La variable <p> representa el precio de venta por unidad.
                    ''',epilog='''
                    En caso de no declarar ningún valor para <p>, se tomará como valor
                    por default de $60/unidad; a su vez, la variable <d> de no señalarse,
                    representará 30 días.
                    '''
                    )
                parser.add_argument('-v','--vminima',help='Venta mínima',type=float,required=True)
                parser.add_argument('-V','--vmaxima',help='Venta máxima',type=float,required=True)
                parser.add_argument('-p','--precio',help='Precio de venta',type=float,required=False)
                parser.add_argument('-d','--dias',help='Número de dias por simular',type=int,required=False)
                args=parser.parse_args()
            elif opt in ("-v","--vminima"):
                try:
                    self.vminima=float(arg)
                except:
                    print('No es posible generar la cantidad solicitada (1)')
                    sys.exit(2)
            elif opt in ("-V","--vmaxima"):
                try:
                    self.vmaxima=float(arg)
                except:
                    print('No es posible generar la cantidad solicitada (2)')
                    sys.exit(2)
            elif opt in ("-p","--precio"):
                try:
                    temporal_precio=float(arg)
                    if temporal_precio<=0:
                        print('No es posible generar la cantidad solicitada (3)')
                        sys.exit(2)
                    self.precio_venta=temporal_precio
                except:
                    print('No es posible generar la cantidad solicitada (4)')
                    sys.exit(2)
            elif opt in ("-d","--dias"):
                try:
                    temporal_dias=int(arg)
                    if temporal_dias<=0:
                        print('No es posible generar la cantidad solicitada (5)')
                        sys.exit(2)
                    self.dias=temporal_dias
                except:
                    print('No es posible generar la cantidad solicitada (6)')
                    sys.exit(2)
        aleatorios.simula(self)
    #Metodo para construir el intervalo
    def simula(self):
        if self.vmaxima<=self.vminima:
            print('No es posible realizar la simulación ')
            sys.exit(2)
            numeros_aleatorios=generar(self.dias)
    #Arreglo en donde se almacenarán los valores del intervalo
            valores=[]
            for j in numeros_aleatorios:
                unidades=round((self.vmaxima-self.vminima)*j+self.vminima,0)
                valores.append(unidades*self.precio_venta)
            self.solucion=valores
def main():
    x=aleatorios(sys.argv[1:])
    data=[] #Arreglo donde estará la información que se manda a archivo
    header=['Dia','Ingreso']
    for i in range(len(x.solucion)):
        data.append([i+1,x.solucion[i]])
    with open('salida.csv','w',encoding='UTF-8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
    print('El archivo ha sido generado')

if __name__ == '__main__':
    main()
