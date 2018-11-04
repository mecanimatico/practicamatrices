#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
print("-----------------------------------------")
print("Matriz A")
"""Dada la matriz A, se hallan los valores y vectores propios
"""
A = np.array([[3,2],
[7, -2]])
print(A)
print("-----------------------------------------")
x,v =np.linalg.eig(A)
print(x,v)
print("Imprime valor y vector propio: ")
print("------------------------------------------")