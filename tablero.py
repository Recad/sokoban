import string
import os
from punto import Puntos


class Tablero(object):

    def __init__(self):
        self.agente = None
        self.muros = set()
        self.tablero = set()
        self.metas = set()
        self.cajas = set()
        self.posiciones = set()
        self.resultado = []


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
        return movimientos

    def mover(self, direccion):#direccion es un objeto de la clase puntos
        ''' mueve al jugador y al jugador y la caja si hay caja '''
        agenteNew = self.agente + direccion


        if agenteNew in self.cajas:
            #print("----------------------------------------------")
            #print ("el agente que esta en "+ str(self.agente))
            #print("se mueve la caja de "+ str(agenteNew))

            self.cajas.remove(agenteNew)
            self.cajas.add(agenteNew + direccion)

            #print("se movio caja a " + str(agenteNew + direccion))
            #aqui se podria evaluar el costo

        self.agente = agenteNew

        self.resultado.append(direccion)


    def printResult(self):

        for i in self.resultado:
            #print(i)

            if i.getX() == -1 and i.getY()== 0:
                print("U")
            elif i.getX() == 1 and i.getY()== 0:
                print("D")
            elif i.getX() == 0 and i.getY()== -1:
                print("L")
            elif i.getX() == 0 and i.getY()== 1:
                print("R")



    def printestadoimport(self):
        print("las cajas estan en :")
        for i in self.cajas:

            print(i)
        print("las metas son :")
        for j in self.metas:
            print(j)

        print("el agente esta en :"+str(self.agente))


        print("los obtaculos son:")
        for k in self.muros:
            print(k)


    def validarWin(self):

        validadorLogico = True

        for i in self.cajas:

            if i in self.metas:

                validadorLogico = (validadorLogico and True)

            else:
                validadorLogico = False

        return validadorLogico


    def validarCaminoRecorrido(self, pos):
        if pos in self.resultado:
            return True
        else:
            return False


'''
x=Tablero()
x.cargarTablero("nivel4.txt")
print(x.posiciones)
print(x.cajas)

'''



