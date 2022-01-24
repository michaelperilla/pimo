from sys import stdin
def soluciones(x,x1):
    global frase1,frase2,dictionary
    if (x,x1) in dictionary:
        return dictionary[(x,x1)]
    if x==0 and x1==0:
        res=0
    elif x==0 and x1>0: 
        res= x1
    elif x>0 and x1==0:
        res= x
    elif frase1[x-1]==frase2[x1-1]:
        res= soluciones(x-1,x1-1)
    else:
        res= min((1+soluciones(x-1,x1-1), (1+soluciones(x-1,x1)),(1+soluciones(x,x1-1))))
    dictionary[(x,x1)]=res
    return res
def main():
    global frase1,frase2,dictionary
    lista=[x for x in stdin.readline().strip().split()]
    while lista:
        x,frase1=lista[0],lista[1]
        x1,frase2=stdin.readline().split()
        dictionary={}
        print(soluciones(int(x),int(x1)))
        lista=[int(x) for x in stdin.readline().strip().split()]
main()

