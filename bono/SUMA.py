from sys import stdin

def suma(ct,ve,x,lista2):
    global lista
    if ct==x:
        if lista2 not in lista:
            lista.append(lista2)
        return 1

    elif len(ve)==0 or ct>x:
        return 0
    else:
        for i in range(len(ve)):
            m=lista2.copy()
            m.append(ve[i])
            ct1=ct+ve[i]
            y=suma(ct,ve[i+1:],x,lista2)
            y1=suma(ct1,ve[i+1:],x,m)
            y2=y+y1
            return y2
def main():
    global lista
    z=stdin.readline().strip().split()
    dato=[]
    i=0
    while i<len(z):
        dato.append(int(z[i]))
        i=i+1
    while dato[1]!=0:
        lista2=[]
        x=dato[0]
        ve=dato[2:]
        lista=[]
        suma(0,ve,x,lista2)
        print("Sums of "+str(x)+":")
        if len(lista)==0:
            print("NONE")
        elif len(lista)!=0:
            print(len(lista))
        z=stdin.readline().strip().split()
        dato=[]
        i=0
        while i<len(z):
            dato.append(int(z[i]))
            i=i+1
main()
                                    
 
