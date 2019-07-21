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




        ##DEBO PONER EL CICLO DE EXPLORACIÓN PRINCIPAL



        ##primero debo validar que hijos puede tener debo crear una función


        ##Aqui expando los hijos pero debo vali
        nodoActual = colaPrincipal.pop(0)

        hijos = nodoActual.moviValidos() #Aqui los hijos que estoy expandiendo


        explorado.add(nodoActual)
        for j in hijos:
            hijoactual = deepcopy(nodoActual) #Este es el que vamos a mover, a convertr en hijo por eso lo copiamos
            nodes_generated += 1
            hijoactual.move(j)
            if hijoactual not in explorado:
                if hijoactual.is_win():
                    #   Que hacer si gana

                    return hijoactual
                colaPrincipal.push(hijoactual)
            else:
                #nodes_repeated += 1 nodos que se repiten


        




