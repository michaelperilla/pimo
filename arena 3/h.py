import collections

class myqueue:
    def __init__(self):
        self.data = collections.deque()

    def peek(self):
        return self.data[0]
    
    def pop(self):
        return self.data.popleft()

    def put(self, value):
        self.data.append(value)

queue = myqueue()
x = int(input())
for i in range(x):
    val = list(map(int,input().split()))
    if val[0] == 1:
        queue.put(val[1])
    elif val[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
