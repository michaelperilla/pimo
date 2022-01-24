from sys import stdin

def f(n,i):
    if i==0:
        return 0
    elif n==0:
        return 1
    elif n<v[i-1]:
        return f(n,i-1)
    else:
        return f(n-v[i-1],i)+f(n,i-1)


def memo(n,i):
    lista=[[0 for c in range(i+1)]for t in range(n+1)]
    for x in range(len(lista)):
        for y in range(len(lista[x])):
            if x==0:
                lista[x][y]=1
            elif y==0:
                lista[x][y]=0
            elif x<v[y-1]:
                lista[x][y]=lista[x][y-1]
            else:
                lista[x][y]=lista[x-v[y-1]][y]+lista[x][y-1]
    return lista[n][i]
            
def main():
    global v
    v=[1,5,10,25,50]
    a=int(stdin.readline())
    fin=memo(a,len(v))
    print(fin)
main()
