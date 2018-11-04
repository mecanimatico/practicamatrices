#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: Heber Pareja Reinoso

"""
Punto 3 del Taller "Escriba una función que genere 
números aleatorios de Cauchy
"""
import numpy as np
import math as m

u=np.random.rand()
print "u: " +str(u)

def f(u):
    a=m.tan(m.pi*(u+float(0.5)))
    return a

print "Función números aleatorios de Cauchy: " +str(f(u))