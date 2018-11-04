#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
A = np.array([[3,1],[2,4]], np.int)
D, V= np.linalg.eig(A)
#Con eig se obtienen los valores y vectores propios
print(" Los valores propios de la matriz de transición son: ")
print(D)
print(" El valor propio asociado a lambda = 1 es :  ")
print(V[:, 1])
print(" Normalizando el vector y multiplicando por el número ")
print(" El vector propio es: ")
print(np.round(2*V[:, 1]/sum(V[:, 1])))

