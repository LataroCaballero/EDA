class Nodo():
    def __init__(self, dato):
        self.__dato = dato
        self.__izq = None
        self.__der = None

    def getDato(self):
        return self.__dato

    def setIzq(self,dato):
        self.__izq = dato

    def getIzq(self):
        return self.__izq

    def setDer(self,dato):
        self.__der = dato

    def getDer(self):
        return self.__der