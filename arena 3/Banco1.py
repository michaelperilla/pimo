from sys import stdin
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
    def Insertar(self,dato):
        temp = Nod(dato)
        if self.vacia():
            self.cabeza = temp
            
        else:
            self.cola.siguiente = temp
            temp.anterior= self.cola
        self.cola = temp
            
    def borrar(self):
        if not self.vacia():
            w = self.cabeza
            if w != None:
                self.cabeza = self.cabeza.siguiente
            return w
    def primero(self):
        temp = self.cabeza
        return temp.verNodo()
def main():
    cases = int(stdin.readline().strip())
    for i in range(cases):
        m = int(stdin.readline().strip())
        banco = Doble()
        for j in range(m):
            entr = stdin.readline().strip()
            if entr == 'Siguiente':
                if banco.vacia():
                    print('No hay fila')
                else:
                    print(banco.primero())
                    banco.borrar()
            else:
                banco.Insertar(entr)
main()

