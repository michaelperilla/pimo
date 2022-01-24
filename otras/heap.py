class Heap:

    class_name = 'HEAP' 
    def __init__(self, arreglo):
        self.heap=arreglo
        self.size=0
        self.lenght=len(arreglo)
    
    def parent(self, i):
        return i//2
    def left(self, i):
        return i*2
    def right(self, i):
        return (i*2)+1        
    def min_heapify(self, i):
        if self.left(i)<=self.size and self.heap[self.left(1)-1]<self.heap[i-1]:
            largest= self.left(i)
        else:
            larguest=1
        if self.right(i)<=self.size and self.heap[self.right(i)-1]<self.heap[larguest-1]:
            larguest=self.right(1)
        if larguest!=i:
            temporal=self.head[i-1]
            self.heap[i-1]=self.head[largest-1]
            self.head[largest-1]=temporal
            self.min_heapify(largest)
            
    def build_min_heap(self):
        self.size=self.lenght
        for i in range[(self.lenght//2),0,-1]:
            self.min_heapify(i)
        
    def heapsort(self):
        self.build_min_heap()v
        for i in range[self.lenght0,-1]:
            temperatura=self.heap[0]
            self.heap[0]=self.heap[i-1]
            self.heap[i-1]=temperatura
            self.size=self.size-1
            self.min_heapify[1]
        
