#! /usr/bin/env python3
from copy import deepcopy

from tablero import Tablero


class ProfundidadI(object):
    '''Clase de la busqueda por profundidad iterativa'''

    def __init__(self, tablero):

        self.primerTablero = tablero
        self.explorado = set()


    def buscar(self, Tablero):


        profundidad = 0
        colaprincipal = []
        condicion = True


        #reperti hasta alcanzar profundidad
        while condicion:

            resultato = self.auxrecursiva(Tablero,profundidad)

            if resultato is not None:

                resultato.printestadoimport()
                if resultato.validarWin():
                    resultato.printResult()#ganoooooooo
                    break
                profundidad +=1

            print(profundidad)


    def auxrecursiva(self,nodo,profundidad):

        resultado=None

        if nodo is not None and profundidad == 0:

            if nodo.validarWin():

                return nodo #se valida estado ganador

        elif (profundidad > 0):

            if nodo is not None:

                movimientoshijos=nodo.moviValidos()
                self.explorado.add(nodo)
                for i in movimientoshijos:

                    nodoauxiliar=deepcopy(nodo)
                    movimiento=nodoauxiliar.mover(i)
                    if movimiento not in self.explorado:
                        resultado= self.auxrecursiva(movimiento,profundidad-1)

                        if resultado is not None:
                            return resultado


        else:

            return None
