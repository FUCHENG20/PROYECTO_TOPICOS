#!/usr/bin/env python
#-*-coding: utf-8 -*-
#
# 
#
# Fucheng Zhou
# Mar/22/22
# al20760444.at.ite.dot.edu.dot.mx

import numpy as np, csv

if __name__ == '__main__':
    pagando = 0
    for i in range(300):
        t = round(np.random.exponential(0.002),3) 
        if t > 0.60:
            pagando+=1
    pagado = round(2125*(pagando/300),2)
    print('Se Pagaron {} ocasiones, con monto promedio de ${}'.format(pagando,pagado))
