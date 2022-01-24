from sys import stdin
def suma(n,i):
    global numeros,conta
    if n==0:
        conta+=1
        return conta
    elif i<0 or n<0:
        return conta
    else:
        suma(n-numeros[i],i-1),suma(n,i-1)
        return conta
def main():
    global numeros,conta
    n=stdin.readline().strip()
    potencia=stdin.readline().strip()
    while n!="" or potencia!="":
        conta=0
        n=int(n)
        power=int(potencia)
        numeros=[]
        for i in range(1,n):
            numeros.append(i**power)
        respuesta=suma(n,len(numeros)-1)
        print(respuesta)
        n=stdin.readline().strip()
        potencia=stdin.readline().strip()
main()
