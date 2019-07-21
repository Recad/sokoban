#! /usr/bin/env python3
import random, math


class Amplitud(object):
    '''Clase de la busqueda por amplitud'''
    #Es estado es si esta infectados o sanos
    #las posicion dentro de la matrix esta dada por x y y


    def __init__(self, partida,llegada,mapa):
        self.__partida = partida
        self.__llegada = llegada
        self.__mapa = mapa



    def CambiarEstado(self, nuevoEstado):
        self.__estado=nuevoEstado #nada


