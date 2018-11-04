#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Multiplicación de matrices
#Estoy importando librerias necesarias al desarrollo del programa
import numpy 
import sys
print ("Multiplicación de Matrices")

#Introduce el número de renglones y columnas de la matriz 1
r1=int(input("Número de renglones matriz 1: "))
c1=int(input("Número de columnas matriz 1: "))

#Introduce el número de renglones y columnas de la matriz 2

r2=int(input("Número de renglones matriz 2: "))
c2=int(input("Número de columnas matriz 2: "))

#Se verifica si se puede realizar la multiplicación

if (c1!=r2):
    print ("No se puede realizar la multiṕlicación")
#El sys.exit() verifica el if y cierra la comparación
    sys.exit()

#Crea la matriz1 de ceros, de tamaño ((r1,c1))

matriz1=numpy.zeros((r1,c1))

#Crea la matriz2 de ceros, de tamaño ((r2,c2))
matriz2=numpy.zeros((r2,c2))

#Define tamaño de la matriz r, resultante
matrizr=numpy.zeros((r1,c2))

#Introduce los elementos de la primera matriz

print ("Por favor introduzca los elementos de la matriz 1: ")
for r in range(0,r1):
    for c in range(0,c1):
        matriz1[(r,c)]=input("Elemento a["+str(r+1)+str(c+1)+"]")

print ("Por favor introduzca los elementos de la matriz 2: ")
for r in range(0,r2):
    for c in range(0,c2):
        matriz2[(r,c)]=input("Elemento a["+str(r+1)+str(c+1)+"]")

#Operaciones de multiplicación

for r in range(0,r1):
    for c in range(0,c2):
        for k in range(0,r2):
            matrizr[(r,c)]+=matriz1[r,k]*matriz2[(k,c)]
print ("La matriz producto es: ")

print (matrizr)
        





