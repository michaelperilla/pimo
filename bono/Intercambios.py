from sys import stdin
def main():
    global ct
    n=int(stdin.readline().strip())
    while n>0:
        l = []
        for k in range(n):
            l.append(int(stdin.readline().strip()))
        ct=[]
        merge(l)
        sol=0
        for i in range(len(ct)):
            sol=sol+ct[i]
        print(sol)
        n=int(stdin.readline().strip())
def merge(lista):
    if(len(lista)<=1):
        return lista
    else:
        left = merge(lista[:len(lista)//2])
        right = merge(lista[len(lista)//2:])
    return sort(left,right)
def sort(left,right):
    x=0
    y=0
    lista2 = []
    while (x<len(left) or y<len(right)):
        if(x>=len(left)):
            lista2.append(right[y])
            y=y+1
        elif(y>=len(right)):
            lista2.append(left[x])
            x=x+1
        else:
            if(left[x]<right[y]):
                 lista2.append(left[x])
                 x=x+1
            else:
                lista2.append(right[y])
                y=y+1
                ct.append(len(left)-x)
    return lista2
    
main()
