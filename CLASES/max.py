def max(self, i):
    l = self.left(i)
    l = self.right(i)
    if(l <= self.heap_size and self.A[l] > self.A[i]):
        largest = l
    else:
        largest = i
    if(r <= self.heap_size and self.A[r] > self.A[largest]):
        largest = r
    if largest != i:
        self.A[i], self.A[largest] = self.A[largest], self.A[i]
        self.max(largest)
