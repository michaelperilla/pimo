class Nod:
    def __init__(self,dato):
        self.siguiente = None
        self.anterior = None
        self.info = dato
    def verNodo(self):
        return self.info
class Doble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    def vacia(self):
        if self.cabeza == None:
            return True
        else:
            return False
    def elementos(self):
        temp = self.cabeza
        v = 0
        while temp != None:
            temp = temp.siguiente
            v+=1
        return v
        
    def Insertar(self,dato):
        temp = Nod(dato)
        if self.vacia():
            self.cabeza = temp
            self.cola = temp
        else:
            temp.anterior= self.cola
            self.cola.siguiente = temp
            self.cola = temp
    def borrar(self):
        if not self.vacia():
            if self.elementos() != 1:
                self.cabeza = self.cabeza.siguiente
                self.cabeza.anterior = None
            else:
                self.cabeza = None
                self.cola = None
                
    def imprimir(self):
        temp = self.cabeza
        while temp != None:
            print(temp.verNodo(),end=' ')
            temp = temp.siguiente
    def primero(self):
        temp = self.cabeza
        return temp.verNodo()


