#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Programa para resolver la matriz de hilbert en python
#Se establece la dimension de la matriz
filas=3
columnas=3
matriz=[]
for i in range(filas):
    matriz.append([0]*columnas)
    print(matriz)

#Se rellena la matriz, así:
contador=1
for i in range(filas):
    for j in range(columnas):
        matriz[i][j]=contador
        contador+=1
#se imprime la matriz
print matriz

    