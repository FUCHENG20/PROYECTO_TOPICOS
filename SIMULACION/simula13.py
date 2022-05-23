#!/usr/bin/python
#-*-coding: utf-8 -*-
#
# Ejemplo para el calculo de la demanda de una revista
#
# Fucheng Zhou
# Mar/17/22
# al20760444.at.ite.dot.edu.dot.mx

import random, numpy as np, scipy.stats
from re import A

def intervalo_confianza(data, confianza=0.95):
    n=len(data)
    m, se=np.mean(data), scipy.stats.sem(data)
    h = se*scipy.stats.t.ppf((1+confianza)/2,n-1)
    return m,n-h,m+h

def main():
    indice_demanda=[]
    for i in range(300):
        rnd = round(random.random(),2)
        if rnd <= 0.05:
            indice_demanda.append(5)
        elif rnd <= 0.1 and rnd >= 0.06:
            indice_demanda.append(6)
        elif rnd <= 0.2 and rnd >= 0.11:
            indice_demanda.append(7)
        elif rnd <= 0.35 and rnd >= 0.21:
            indice_demanda.append(8)
        elif rnd <= 0.6 and rnd >= 0.36:
            indice_demanda.append(9)
        elif rnd <= 0.85 and rnd >= 0.61:
            indice_demanda.append(10)
        elif rnd <= 1 and rnd >= 0.86:
            indice_demanda.append(11)
    intervalo_confianza(indice_demanda)
    demanda_promedio,demanda_minima,demanda_maxima = intervalo_confianza (indice_demanda)
    print("La demanda esta entre {} y {}".format(demanda_minima, demanda_maxima, 2))
    
            

if __name__ == '__main__':
    main()