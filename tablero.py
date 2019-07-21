import string
import os
from punto import Puntos


class Tablero(object):

    '''
    Board's overloaded functions and functions for
    board manipulation live here
    '''

    def __init__(self):
        #self.dir_list = dir_list  # aun no esta claro
        self.tablero = set()
        self.muros = set()
        self.posiciones= set()
        self.metas = set()
        self.cajas = set()
        self.agente = ""
        #self.cost = 1  # no se usa


    def cargarTablero(self, archivo):
        #viteri aca coloca lo de leer de un archivo y llenar las listas con su rrespectivo item
        #puto el que lo lea
        ruta = os.getcwd() + "/" + archivo
        g = open(ruta, 'r')
        fila = 0
        contador = 0
        coordenada = ""
        for linea in g.readlines():
            columna = 0
            fila = fila + 1
            posic = ''
            for letra in linea:
                columna = columna + 1
                if letra != '\n':
                    if letra == "0":
                        self.posiciones.add(Puntos(fila,columna))
                    elif letra == "W":
                        self.muros.add(Puntos(fila,columna))
                    elif letra == "X":
                        self.metas.add(Puntos(fila,columna))
                    else:
                        contador = contador + 1
                        if contador <= 3:
                            self.agente = self.agente + letra
                        else:
                            posic = posic + letra
            cajasObjeto(self,posic)
        agenteObjeto(self)

def cajasObjeto(self,posicion):
    if posicion != '':
        self.cajas.add(Puntos(posicion[0],posicion[2]))

def agenteObjeto(self):
    self.agente = Puntos(self.agente[0], self.agente[2])


x=Tablero()
x.cargarTablero("nivel4.txt")
print(x.posiciones)
print(x.cajas)





