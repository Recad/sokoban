#! /usr/bin/env python3
import string
import os

tablero_sp = {}
tablero_cp = {}
def leerTablero():
	ruta = os.getcwd() + "/nivel4.txt"
	contador = -1
	g = open(ruta , "r")
	for linea in g.readlines():
		contador = contador + 1
		tablero_sp[contador] = []
		for letra in linea:
			if letra != '\n':
				tablero_sp[contador].append(letra)
	posiciones(tablero_sp)

def posiciones(mapa):
	contador = 0
	for key in mapa.keys():
		if mapa[key][1] == ',':
			if contador == 0:
				contador = contador + 1
				mapa[int(mapa[key][0])][int(mapa[key][2])] = "J"
			else:
				mapa[int(mapa[key][0])][int(mapa[key][2])] = "C"
				print(mapa[key][2])
	tablero_cp = mapa
	print(tablero_sp)

leerTablero()
