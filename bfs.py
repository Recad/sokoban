#! /usr/bin/env python3
from copy import deepcopy


from tablero import Tablero


class Amplitud(object):
    '''Clase de la busqueda por amplitud'''



    def __init__(self,tablero):

       self.primerTablero = tablero



    def buscar(self, Tablero):

        node = deepcopy(Tablero)
        nodes_generated = 0
        #Aqui se mete el primer elemento de la cola, recordar que en bfs se añaden los hijos al final
        colaPrincipal = []
        colaPrincipal.insert(0, node)
        explorado = set()


        condicion = True

        ##DEBO PONER EL CICLO DE EXPLORACIÓN PRINCIPAL

        while condicion: #no encuentro la condicion



            ##primero debo validar que hijos puede tener debo crear una función

            print(" cola antes del pop es :" + str(len(colaPrincipal)))
            ##Aqui expando los hijos pero debo vali
            nodoActual = colaPrincipal.pop(0)
            print(" cola despues del pop es :" + str(len(colaPrincipal)))
            nodoActual.printestadoimport()
            hijos = nodoActual.moviValidos() #Aqui los hijos que estoy expandiendo


            explorado.add(nodoActual)
            for j in hijos:
                hijoactual = deepcopy(nodoActual) #Este es el que vamos a mover, a convertr en hijo por eso lo copiamos
                nodes_generated += 1
                hijoactual.mover(j)

                print("el hijo actual es: " + str(hijoactual) +":")

                if hijoactual not in explorado:
                    if hijoactual.validarWin():
                        #   Que hacer si gana
                        print("GANASTE PUTOOO")
                        condicion=False
                        return hijoactual
                        break
                    colaPrincipal.insert(0, hijoactual)
                else:
                    #nodes_repeated += 1 nodos que se repiten
                    print("No se que decir")


        




