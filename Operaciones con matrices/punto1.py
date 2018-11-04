#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Heber Pareja Reinoso

"""
Solución punto 1
"""
import numpy as np
from random import randint, uniform, random

p1 = float(input("Ingrese el valor p1: "))
p2 = float(input("Ingrese el valor p2: "))

delta1 = float(input("Ingrese delta1: "))
delta2 = float(input("Ingrese delta2: "))

u=np.random.rand()

def f(p1,p2,delta1,delta2):
    a=(u<=p1)*delta1+(u<=p1+p2 and u>p1)*(-delta2)
    return a

print "Número aleatorio: " +str(u)
print "X: " +str(f(p1,p2,delta1,delta2))


