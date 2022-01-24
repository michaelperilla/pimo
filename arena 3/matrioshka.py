from sys import stdin
while True:
    x = True
    y = True
    a = stdin.readline().strip().split()
    if a == []:
        break
    a = list(map(int,a))
    
    conta = []
    index = []
    index.append(a[0])
    conta.append(abs(a[0]))
    for i in range(len(a)-1):
        if a[i+1] < 0:
            index.append(a[i+1])
            conta[-1] += a[i+1]
            if conta[-1] <= 0:
                break
            conta.append(abs(a[i+1]))
        else:
            if a[i+1] == -1*index[-1]:
                index.pop()
                conta.pop()
            else:
                break
           
    if len(index) == 0:
        print(':-) Matrioshka!')
    else:
        print(':-( Try again.')
        
        
