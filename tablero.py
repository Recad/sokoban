import string
import os
from spot import Spot
from direction import Direction

'''tener en consideración esto'''
'''L = Direction(Spot(-1, 0), 'l')
R = Direction(Spot(1, 0), 'r')
U = Direction(Spot(0, -1), 'u')
D = Direction(Spot(0, 1), 'd')
directions = [U, D, L, R]'''

class Tablero(object):

    '''
    Board's overloaded functions and functions for
    board manipulation live here
    '''

    def __init__(self):
        #self.dir_list = dir_list  # aun no esta claro
        self.tablero = set()
        self.muros = set()
        self.posiciones= set()
        self.metas = set()
        self.cajas = set()
        self.jugador = ""
        self.agente = None
        #self.cost = 1  # no se usa


    def cargarTablero(self, archivo):
        #viteri aca coloca lo de leer de un archivo y llenar las listas con su rrespectivo item
        #puto el que lo lea
        ruta = os.getcwd() + "/" + archivo
        g = open(ruta, 'r')
        fila = 0
        contador = 0
        coordenada = ""
        for linea in g.readlines():
            columna = 0
            fila = fila + 1
            posic = ''
            for letra in linea:
                columna = columna + 1
                if letra != '\n':
                    if letra == "0":
                        self.posiciones.add( str(fila) + "," + str(columna))
                    elif letra == "W":
                        self.muros.add( str(fila) + "," + str(columna))
                    elif letra == "X":
                        self.metas.add( str(fila) + "," + str(columna))
                    else:
                        contador = contador + 1
                        if contador <= 3:
                            self.jugador = self.jugador + letra
                        else:
                            posic = posic + letra
            self.cajas.add(posic)








