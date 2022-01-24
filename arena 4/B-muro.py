from sys import stdin

def sol(x,lista):
    for j in range(2,70):
        lista[j] = lista[j-2]+lista[j-1]
    while x!=0:
        print(lista[x-1])
        x = stdin.readline().strip()
        x = int(x)

def  main():
    x = stdin.readline().strip()
    x = int(x)
    lista=[1]*70
    lista[1]=2
    sol(x, lista)
main()
