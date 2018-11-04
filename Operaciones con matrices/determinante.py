#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
"""
Resuelve el determinante de una matriz dada
"""
print("Matriz A: ")
A = np.array([[1,2,3],[2,-2,4],[2,2,5]])
print(A)

print("--------------------------------------------")
determinante = np.linalg.det(A)
print("El determinante de la matriz A, es:  ")
print(determinante)
print("--------------------------------------------")
