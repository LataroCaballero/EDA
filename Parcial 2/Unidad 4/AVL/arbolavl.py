from nodo import Nodo
from __future__ import print_function

class ArbolAVL():
    def __init__(self):
        self.__raiz = None
        self.__cant = 0

    def insertar(self, dato):
        nuevo = Nodo(dato)

        if self.__raiz == None:
            self.__raiz = nuevo
            self.__raiz.setAltura(0)
            self.__cant = 1
        else:
            padre = None
            actual = self.__raiz
            band = True

            while band:
                if actual != None:
                    padre = actual
                    
                    if nuevo.getDato() < actual.getDato:
                        actual = actual.getIzq()
                    elif nuevo.getDato() > actual.getDato:
                        actual = actual.getDer()
                else:
                    nuevo.setAltura(padre.getAltura())
                    padre.setAltura(padre.getAltura() + 1)
                    if nuevo.getDato() < padre.getDato():
                        padre.setIzq(nuevo)
                    else:
                        padre.setDer(nuevo)
                    self.rebalancear(nuevo)
                    self.__cant += 1
                    band = False

    def rebalancear(self, nodo):
        n = nodo

        while n != None:
            altDer = n.getAltura()
            altIzq = n.getAltura()

            if n.getDer()!= None:
                d = n.getDer()
                altDer = d.getAltura()

            if n.getIzq()!= None:
                i = n.getIzq()
                altIzq = i.getAltura()
            
            if abs(altIzq - altDer) > 1:
                if altIzq > altDer:
                    hijIzq = n.getIzq()
                    if hijIzq != None:
                        