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

    def __init__(self, dir_list):
        #self.dir_list = dir_list  # aun no esta claro
        self.muros = set()
        self.posiciones= set()
        self.metas = set()
        self.cajas = set()
        self.agente = None
        #self.cost = 1  # no se usa


    def cargarTablero(self):
        #viteri aca coloca lo de leer de un archivo y llenar las listas con su rrespectivo item
        #puto el que lo lea