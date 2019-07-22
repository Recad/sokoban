#! /usr/bin/env python3
from copy import deepcopy


from tablero import Tablero


class Amplitud(object):
    '''Clase de la busqueda por amplitud'''



    def __init__(self,tablero):

       self.primerTablero = tablero



    def buscar(self, Tablero):

        nodocopia = deepcopy(Tablero)
        estadoinicial = deepcopy(Tablero)
        #Aqui se mete el primer elemento de la cola, recordar que en bfs se añaden los hijos al final
        colaPrincipal = []
        colaPrincipal.insert(0, nodocopia)
        explorado = set()
        #profundidad = 0

        condicion = True

        ##DEBO PONER EL CICLO DE EXPLORACIÓN PRINCIPAL

        while condicion : #no encuentro la condicion
            #profundidad += 1
            if len(colaPrincipal)== 0:
                print("no se pudo encontrar una solucion")
                break
            ##primero debo validar que hijos puede tener debo crear una función


            ##Aqui expando los hijos pero debo vali

            nodoEvaluar = colaPrincipal.pop(0)



            #nodoEvaluar.printestadoimport()

            posicioneshijos = nodoEvaluar.moviValidos() #Aqui los hijos que estoy expandiendo


            explorado.add(nodoEvaluar)

            for j in posicioneshijos:
                '''A cada hijo debo avaluarlo y enviarlo al final de la cola'''

                hijoactual = deepcopy(nodoEvaluar) #Este es el que vamos a mover, a convertr en hijo por eso lo copiamos
                hijoactual.mover(j)

                #and hijoactual != estadoinicial
                if hijoactual not in explorado :

                    if hijoactual.validarWin():
                        #   Que hacer si gana


                        condicion=False
                        hijoactual.printResult()
                        #return hijoactual

                    valueins = len(colaPrincipal) - 1
                    colaPrincipal.insert(valueins, hijoactual)




        




