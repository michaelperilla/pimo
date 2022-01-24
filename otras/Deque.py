class node():
    def __init__(self ,x):
        self.val = x
        self.der = None
        self.izq = None
class Deque():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tam = 0
    def append_right(self,x):
        nodo = node(x)
        if self.ultimo == None:
            self.primero = self.ultimo = nodo
        else:
            self.ultimo.der = nodo
            nodo.izq = self.ultimo
            self.ultimo = nodo
        self.tam+=1
    def append_left(self, x):
        nodo = node(x)
        if self.primero == None:
            self.primero = self.ultimo = nodo
        else:
            self.primero.izq = nodo
            nodo.der = self.primero
            self.primero = nodo
        self.tam+=1
    def pop_right(self):
        x = self.ultimo.val
        if self.ultimo == None:
            raise Exception("Impisible hacer pop")
        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            penultimo = self.ultimo.izq
            self.ultimo = None
            self.ultimo = penultimo
        self.tam-=1
        return x
    
    def pop_left(self):
        x = self.primero.val
        if self.ultimo == None:
            raise Exception("Impisible hacer pop")
        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            segundo = self.primero.der
            self.primero = None
            self.primero = segundo
        self.tam-=1
        return x
    
    def valores(self):
        nodo = self.primero
        res = []
        while nodo != None:
            res.append(nodo.val)
            nodo = nodo.der
        return res
    def __len__(self):
        return self.tam

q = Deque()
print(q.valores())
q.append_right(3); print(q.valores())
print(q.pop_right(),"POP") ; print(q.valores())
q.append_right(2) ; print(q.valores())
q.append_right(5) ; print(q.valores())
print(q.pop_right(),"POP"); print(q.valores())
q.append_left(1) ; print(q.valores())
q.append_left(0); print(q.valores())
print(q.pop_right(),"POP"); print(q.valores())
q.append_right(0); print(q.valores())
print(len(q))
            
