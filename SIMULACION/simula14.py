#!/usr/bin/env python
#-*-coding: utf-8 -*-
#
# Ejemplo para el calculo de pago de una aseguradora
#
# Fucheng Zhou
# Mar/22/22
# al20760444.at.ite.dot.edu.dot.mx

import random, csv


if __name__=='__main__':
    pagos=[]
    for i in range(300):
        rnd=round(random.random(),2)
        if rnd<=.60:
            pagos.append(0)
        elif rnd>=.61 and rnd<=.8:
            pagos.append(500)
        elif rnd>=.81 and rnd<=.9:
            pagos.append(1000)
        elif rnd>=.91 and rnd<=.95:
            pagos.append(2000)
        else:
            pagos.append(5000)

    data=[] #Arreglo donde estará la información que se manda a archivo
    header=['Pago']
    for i in range(len(pagos)):
        data.append([i+1,pagos[i]])
    with open('salida2.csv','w',encoding='UTF-8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
    print('El archivo ha sido generado')