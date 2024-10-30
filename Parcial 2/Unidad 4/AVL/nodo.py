class Nodo():
    def __init__(self, dato):
        self.__dato = dato
        self.__padre = None
        self.__izq = None
        self.__der = None
        self.__altura = None

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

    def setPadre(self, dato):
        self.__padre = dato
    
    def getPadre(self):
        return self.__padre

    def setAltura(self, altura):
        self.__altura = altura
    
    def getAltura(self)
        return self.__altura