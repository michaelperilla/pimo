from sys import stdin

def menu(n, ct):
    if(n == 1):
        return(ct+1)
    else:
        if(n%2 ==1):
            n = 3*n+1
            ct += 1
            return menu(n,ct)
        else:
            n = n/2
            ct += 1
            return menu(n,ct)

def main():
    z= stdin.readline().strip()
    while( z != ""):
        x,x1 = z.split()
        x = int(x)
        x1 = int(x1)
        if(x>x1):
            lista = list(range(x1,x+1))
        elif(x==x1):
            lista = list(range(x,x1+1))
        else:
            lista = list(range(x,x1+1))
        mayor = 0
        for i in lista:
            
            a=(menu(i,0))
            if (a>mayor):
                mayor = a
            
        print(x,x1,mayor)
        z = stdin.readline().strip()
main()
