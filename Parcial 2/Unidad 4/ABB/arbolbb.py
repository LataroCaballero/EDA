from nodo import Nodo

class ArbolBB():
    def __init__(self, dato):
        self.__raiz = Nodo(dato)
    
    def __insertar_recursivo(self, nodo, dato):
        if dato < nodo.getDato():
            if nodo.getIzq() == None:
                nuevo = Nodo(Dato)
                nodo.setIzq(nuevo)
            else:
                insertar_recursivo(nodo.getIzq(), dato)
        elif dato > nodo.getDato():
            if nodo.getDer() == None:
                nuevo = Nodo(dato)
                nodo.setDer(dato)
            else:
                insertar_recursivo(nodo.getDer(), dato)
        else:
            return "[!] El dato ya existe en el arbol"
        
    def __preorder_recursivo(self, nodo):
        if nodo != None:
            print(nodo.getDato, end=", ")
            preorder(nodo.getIzq())
            preorder(nodo.getDer())

    def __inorder_recursivo(self, nodo):
        if nodo != None:
            inorder(nodo.getIzq())
            print(nodo.getDato, end=", ")
            inorder(nodo.getDer())
    
    def __postorder_recursivo(self, nodo):
        if nodo != None:
            postorder(nodo.getIzq())
            postorder(nodo.getDer())
            print(nodo.getDato, end=", ")

    def __buscar_recursivo(self, nodo, dato):
        if nodo == None:
            return None
        if nodo.getDato == dato:
            return nodo
        if dato < nodo.getDato():
            return self.__buscar(nodo.getIzq(), dato)
        else:
            return self.__buscar(nodo.getDer(), dato)

    def insertar(self, dato):
        self.__insertar_recursivo(self.__raiz, dato)
    
    def inorder(self):
        print("Imprimiendo arbol inorder")
        self.__inorder_recursivo(self.__raiz)
        print("")
    
    def preorder(self):
        print("Imprimiendo arbol preorder")
        self.__preorder_recursivo(self.__raiz)
        print("")

    def postorder(self):
        print("Imprimiendo arbol postorder")
        self.__postorder_recursivo(self.__raiz)
        print("")

    def buscar(self, dato):
        return self.__buscar_recursivo(self.__raiz, dato)