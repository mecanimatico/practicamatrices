#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Heber Pareja Reinoso
Se importan librerias numpy y matemáticas
"""
import numpy as np
import math as m
"""
Se ingresan las variables de entrada
"""
print "----------------------------------------------"
sigma1= float(input('Ingrese el valor de sigma1: '))
sigma2= float(input('Ingrese el valor de sigma2: '))
rho= float(input('Ingrese coeficiente de correlación: '))
itera=(input('Ingrese el número de iteraciones deseado: '))
print "----------------------------------------------"
"""
Se lleva la cuenta de ciclos hasta el número de iteraciones enteras.
"""
contador = 1
while contador<=itera:
    contador=contador+1
    u = np.random.rand(2,1)
    """
    Se define matriz de varianza y covarianza
    """
    matrix = np.array([
        [sigma1, 0],
        [rho*sigma2,sigma2*m.sqrt(1-rho**2)]
        ])
    solucion = matrix.dot(u)
    """
    Se imprime la solución
    """
    print(solucion)
    print('------------------------------------------')

