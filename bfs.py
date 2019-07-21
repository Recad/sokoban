#! /usr/bin/env python3
from copy import deepcopy

from tablero import Tablero


class Amplitud(object):
    '''Clase de la busqueda por amplitud'''



    def __init__(self, partida,llegada,mapa):
        self.__partida = partida
        self.__llegada = llegada
        self.__mapa = mapa



    def buscar(self, Tablero):

        node = deepcopy(Tablero)
        nodes_generated = 0
        #Aqui se mete el primer elemento de la cola, recordar que en bfs se añaden los hijos al final
        colaPrincipal = set()
        colaPrincipal.push(node)
        explorado = set()


        ##primero debo validar que hijos puede tener debo crear una función


        ##Aqui expando los hijos pero debo vali





        




