from sys import stdin
## Funcion recursiva para implementar la memorizacion 
M=[1,5,10,25,50]
##def f(n,i):
##    global M
##    if n == 0:
##        return 1
##    elif i == 0:
##        return  0
##    elif M[i-1]>n:
##        return f(n,i-1)
##    else:
##        return f(n-M[i-1] ,i) + f( n, i-1)
    
def monedas(n,i):
    a=[[0 for x in range(i+1)]for y in range(n+1)]
    global M
    for d in range(len(a)):
        for z in range(len(a[d])):
            
            if d == 0:
                a[d][z]=1
            elif z==0:
                a[d][z]=0
            elif M[z-1]>d:
                a[d][z]= a[d][z-1]
            else:
                a[d][z]= a[d-M[z-1]][z] + a[d][z-1]

               
    return a 
            

def main():
    x=monedas(30000,5)
    a= stdin.readline().strip()
    while a != "":
        a=int(a)
##        fin1=f(a,5)
        fin = x[a][5]
        if fin == 1:
            print("There is only "+str(fin)+" way to produce "+str(a)+" cents change.")
        else:
            print("There are "+str(fin)+" ways to produce "+str(a)+" cents change.")
        a= stdin.readline().strip()
main()
#Problema desaroyado en la monitoria del dia 12/2/2018
