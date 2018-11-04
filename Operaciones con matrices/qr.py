#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
print("Matriz dada A: ")
A=np.array([[1,2],[3,1]])
print(A)
print('--------------------------------------------------')

a1 = (A[:,0])
print(a1)
u1=a1
e1 = u1/(np.linalg.norm(u1))
print(e1)
print "Vector normalizado e1: " +str(e1)
print('--------------------------------------------------')

a2 = (A[:,1])
print(a2)
u2=a2-np.dot(a2,e1)*e1
e2= u2/(np.linalg.norm(u2))
print(e2)
print "Vector normalizado e2: " +str(e2)
print('------------------------------------------------')

"""
Cambio de dimensión los vectores e1, e2
"""
e1 = e1.reshape(2,1)
e2 = e2.reshape(2,1)
"""
Construye la matriz cuyas entradas son e1 y e2 y el 1 las coloca en columna
"""
Q=np.append(e1,e2,1)
print("Q: ")
print(Q)
print("----------------------------------------------")

R=np.array([
    [np.dot(a1,e1)[0],np.dot(a2,e1)[0]],
    [0,np.dot(a2,e2)[0]]
    ])
print("R: ")
print(R)
print("---------------------------------------------")
S=Q.dot(R)
print(S) 
print("S = A , matriz dada: ")
print("---------------------------------------------")

