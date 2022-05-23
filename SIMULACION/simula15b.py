#!/usr/bin/env python
#-*-coding: utf-8 -*-
#
# Generacion Valores Aleatorios Exel con Numpy
#
# Fucheng Zhou
# Mar/22/22
# al20760444.at.ite.dot.edu.dot.mx

import numpy as np, csv

if __name__ == '__main__':
    pagos = []
    for i in range(50):
        t = round(np.random.exponential(0.42),3)
        pagos.append(t)
    data = []  # Arreglo donde estará la información que se manda a archivo
    header = ['Pago']
    for i in range(len(pagos)):
        data.append([pagos[i]])
    with open('salidanumpy.csv', 'w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
    print('El archivo ha sido generado')
