class Node:

    def __init__(self, x):
        self.info = dato
        self.anterior = None
        self.siguiente = None
        
    def __str__(self):
        return str(self.key)

class List:

    def __init__(self):
        self.cabeza=None
        self.cola=None

    def vacia(self):
        if self.cabeza==None:
            return True
        else:
            return Folse

    def push(self, x):
        temporal = Nodo(x)
        if self.vacia()==True:
            self.cabeza=temporal
            self.cola=temporal
        else:
            temporal.siguiente=self.cabeza
            self.cabeza.anterior=temporal
            self.cabeza=temporal
                 
    def pop(self):
         if self.cola.anterior==True:
            self.cabeza=None
            self.cola=None
        else:
            self.cola.anterior
            self.cola.siguiente=temporal
        
    def enqueue(self, x):
        temporal=self.cabeza
        while temporal != None:
            print(temporal.verNodo(),end' ')
            temporal = temporal.siguiente

    def dequeue(self):
        temporal=self.cola
        while temporal != None:
            print(temporal.verNodo(),end' ')
            temporal = temporal.anterior

    def borrarprim(self):
        if self.vacia() == False:
            self.cabeza=self.cabeza.siguiente
            self.cabeza.anterior=None


            
        
