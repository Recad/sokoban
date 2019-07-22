#! /usr/bin/env python3
from copy import deepcopy

from tablero import Tablero


class ProfundidadI(object):
    '''Clase de la busqueda por profundidad iterativa'''

    def __init__(self, tablero):

        self.primerTablero = tablero
        self.explorado = set()


    def buscar(self, Tablero):


        profundidad = 1
        colaprincipal = []
        condicion = True
        resultadonivel = set()

        #reperti hasta alcanzar profundidad
        while condicion:

            resultadonivel = self.auxiter(Tablero,profundidad)

            for i in resultadonivel:

                if i.validarWin():
                    i.printResult()
                    condicion = False
                    break



            profundidad +=1


    def auxiter(self,nodo,profundidad):

        contador=0
        node = deepcopy(nodo)
        # Aqui se mete el ultimo elemento de la cola, recordar que en dfs se añaden los hijos al comienzo
        colaPrincipal = []
        colaPrincipal.insert(0, node)
        explorado = set()




        while contador < profundidad:

            if len(colaPrincipal)== 0:
                print("no se pudo encontrar una solucion")
                break


            ##primero debo validar que hijos puede tener debo crear una función
            nodoEvaluar = colaPrincipal.pop(0)

            # nodoEvaluar.printestadoimport()

            posicioneshijos = nodoEvaluar.moviValidos()  # Aqui los hijos que estoy expandiendo

            explorado.add(nodoEvaluar)

            for j in posicioneshijos:
                '''A cada hijo debo avaluarlo y enviarlo al principio de la cola'''

                hijoactual = deepcopy(nodoEvaluar)  # Este es el que vamos a mover, a convertr en hijo por eso lo copiamos

                hijoactual.mover(j)

                if hijoactual not in explorado:

                    colaPrincipal.insert(0, hijoactual)
            contador +=1


        return explorado


















