#! /usr/bin/env python3
from copy import deepcopy
import heapq

from tablero import Tablero


class Profundidad(object):


    def __init__(self,tablero):

       self.primerTablero = tablero




    def buscar(self,Tablero):
        node = deepcopy(Tablero)
        # Aqui se mete el ultimo elemento de la cola, recordar que en dfs se añaden los hijos al comienzo
        colaPrincipal = []
        colaPrincipal.insert(0, node)
        explorado = set()

        nodosExplorados = []
        condicion = True

        ##CICLO DE EXPLORACIÓN PRINCIPAL
        while condicion:
            if len(colaPrincipal)== 0:
                print("no se pudo encontrar una solucion")
                break

            ##primero debo validar que hijos puede tener debo crear una función
            nodoEvaluar = colaPrincipal.pop(0)

            #nodoEvaluar.printestadoimport()

            posicioneshijos = nodoEvaluar.moviValidos() #Aqui los hijos que estoy expandiendo


            explorado.add(nodoEvaluar)

            for j in posicioneshijos:
                '''A cada hijo debo avaluarlo y enviarlo al principio de la cola'''


                hijoactual = deepcopy(nodoEvaluar) #Este es el que vamos a mover, a convertr en hijo por eso lo copiamos


                hijoactual.mover(j)



                if hijoactual not in explorado:

                	#if hijoactual.validarCaminoRecorrido(j):
                	#	break

                    if hijoactual.validarWin():
                        #   Que hacer si gana
                        condicion=False
                        hijoactual.printResult()
                        #return hijoactual

                    ##valueins = len(colaPrincipal) - 1
                    colaPrincipal.insert(0, hijoactual)





