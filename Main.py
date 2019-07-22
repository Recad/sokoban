#! /usr/bin/env python3
from asyncore import file_dispatcher

from tablero import Tablero
from bfs import Amplitud
from dfs import Profundidad
import bfs
import re
import sys

def main():

	file_name = sys.argv[1]
	newtablero = Tablero()
	amplitud = Amplitud(newtablero)

	profundidad = Profundidad(newtablero)

	newtablero.cargarTablero(file_name)
	amplitud.buscar(newtablero)
	#profundidad.buscar(newtablero)
	print(file_name)














if __name__ == '__main__':
    main()