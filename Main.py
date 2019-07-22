#! /usr/bin/env python3
from asyncore import file_dispatcher

from tablero import Tablero
from bfs import Amplitud
from dfs import Profundidad
from iidfs import ProfundidadI
import bfs
import re
import sys

def main():

	file_name = sys.argv[1]
	algoritmo = int(sys.argv[2])
	newtablero = Tablero()
	amplitud = Amplitud(newtablero)

	profundidad = Profundidad(newtablero)

	iterativa = ProfundidadI(newtablero)

	newtablero.cargarTablero(file_name)

	if algoritmo == 1:
		amplitud.buscar(newtablero)

	elif algoritmo == 2:
		profundidad.buscar(newtablero)

	elif algoritmo == 3:
		iterativa.buscar(newtablero)

	else:
		print("No se definio algoritmo")


if __name__ == '__main__':
    main()