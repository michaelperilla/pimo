class Stack:
    def __init__(self, n):
        self.top = 0
        self.data = [0 for x in range(0,n)]
    def stack_empty(self):
        if self.top == 0:
            return True
        else:return False

    def push(self, x):
        try:
            self.data[self.top] = x
            self.top = self.top + 1
        except IndexError:
            print('La pila esta llena')
    

    def pop(self):
        if self.stack_empty():
            print('Empty Stack')
        else:
            self.top = self.top - 1
            return self.data[self.top]

    
            
