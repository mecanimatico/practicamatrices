#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from numpy import linalg 
# Se declara la matriz de transición,como número de 64 bits

A = np.array([[1,-1,4 ],[3,2,-1],[2,1,-1]], np.float)
print(A)
# Defino la matriz de estado iniicial x0
x0 = np.array([[1],[0],[0]])
# Para calcular A elevado a la 5 se realiza lo siguiente
y = linalg.matrix_power(A,5)
xk = np.dot(y,x0)
print(" El vector propio asociado es: ")
print(xk.round())
