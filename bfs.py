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


            ##Aqui expando los hijos pero debo vali

            nodoEvaluar = colaPrincipal.pop(0)



            #nodoEvaluar.printestadoimport()

            posicioneshijos = nodoEvaluar.moviValidos() #Aqui los hijos que estoy expandiendo


            explorado.add(nodoEvaluar)

            for j in posicioneshijos:
                '''A cada hijo debo avaluarlo y enviarlo al final de la cola'''


                hijoactual = deepcopy(nodoEvaluar) #Este es el que vamos a mover, a convertr en hijo por eso lo copiamos
                nodes_generated += 1

                hijoactual.mover(j)


                if hijoactual not in explorado:

                    if hijoactual.validarWin():
                        #   Que hacer si gana


                        condicion=False
                        hijoactual.printResult()
                        #return hijoactual



                    valueins = len(colaPrincipal) - 1
                    colaPrincipal.insert(valueins, hijoactual)
                else:
                    #nodes_repeated += 1 nodos que se repiten
                    print("No se que decir")


        




