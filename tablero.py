import string
import os
from punto import Puntos


class Tablero(object):

    def __init__(self):
        #self.dir_list = dir_list  # aun no esta claro
        self.tablero = set()
        self.muros = set()
        self.posiciones= set()
        self.metas = set()
        self.cajas = set()
        self.agente = None
        #self.cost = 1  # no se usa

    def cajasObjeto(self, posicion):
            if posicion != '':
                self.cajas.add(Puntos(int(posicion[0]),int(posicion[2])))

    def agenteObjeto(self,agenteTexto):
        self.agente = Puntos(int(agenteTexto[0]),int(agenteTexto[2]))


    def cargarTablero(self, archivo):
        #viteri aca coloca lo de leer de un archivo y llenar las listas con su rrespectivo item
        #puto el que lo lea
        ruta = os.getcwd() + "/" + archivo
        g = open(ruta, 'r')
        fila = 0
        contador = 0
        coordenada = ""
        agenteTexto= ""
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
                            agenteTexto = agenteTexto + letra
                        else:
                            posic = posic + letra
            self.cajasObjeto(posic)
        self.agenteObjeto(agenteTexto)

        print(self.agente)
        print(self.cajas)



    def moviValidos(self):

        movimientos = []
        direcciones = [Puntos(-1, 0),Puntos(1, 0),Puntos(0, -1),Puntos(0, 1)]

        for i in direcciones:
            if self.agente + i not in self.muros:
                if self.agente + i in self.cajas:
                    # y si hay una caja o un muro detras de el?
                    if self.agente + i.double() not in self.cajas.union(self.muros):
                        movimientos.append(i)
                else:
                    movimientos.append(i)

        print("Los movimientos validos para:" + str(self.agente))


        for j in movimientos:
            print(str(j))

        return movimientos

    def mover(self, direccion):#direccion es un objeto de la clase puntos
        ''' mueve al jugador y al jugador y la caja si hay caja '''
        agenteNew = self.agente + direccion
        if agenteNew in self.cajas:
            self.cajas.remove(agenteNew)
            self.cajas.add(agenteNew + direccion)

            #aqui se podria evaluar el costo

        self.agente = agenteNew
        #aqui se puede guardar la direccionself.dir_list.append(direccion)

    def printestadoimport(self):
        print("las cajas estan en :")
        for i in self.cajas:

            print(i)
        print("las metas son :")
        for j in self.metas:
            print(j)

        print("el agente esta en :"+str(self.agente))


    def validarWin(self):

        validadorLogico = True

        for i in self.cajas:

            if i in self.metas:

                print("el valor de i es :"+i)

                validadorLogico = (validadorLogico and True)

            else:
                validadorLogico = False

        return validadorLogico


'''
x=Tablero()
x.cargarTablero("nivel4.txt")
print(x.posiciones)
print(x.cajas)

'''



