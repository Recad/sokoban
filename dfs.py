#! /usr/bin/env python3
from copy import deepcopy
import heapq

from tablero import Tablero


class Profundidad(object):


    def __init__(self,tablero):

       self.primerTablero = tablero




    def buscar(self,Tablero):
        node = deepcopy(Tablero)
        
        # Aqui se mete el primer elemento de la cola, recordar que en bfs se añaden los hijos al final
        colaPrincipal = []
        colaPrincipal.insert(0, node)
        explorado = set()

        condicion = True


