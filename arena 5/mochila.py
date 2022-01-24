from sys import stdin

def cambio(moneda,lista_monedas):
    """Pre: funcion que resive el valor de la moneda y la lista de monedas que son los cambios
       Pos: funcion que retorna las posibles devoluciones o cambio con esa moneda"""
    combinaciones = [[0]*moneda for y in range(len(lista_monedas)+1)]
    #print(combinaciones)
    for x in range(len(lista_monedas)):
        #print(combinaciones)
        #print("..............")
        for i in range(1,moneda):
            #print("************************")
            if i>=lista_monedas[x][0]:
                #print("i",i)
                #print("x",x)
                #print("x[0]",lista_monedas[x][0])
                #print("i",i)
                #print("x[1]",lista_monedas[x][1])
                #print("(x[1]+combinaciones[i-1][i-x[0]])",(lista_monedas[x][1]+combinaciones[x][i-lista_monedas[x][0]]))
                #print("combinaciones[i-1][i]",combinaciones[x][i])
                combinaciones[x+1][i]+=max((lista_monedas[x][1]+combinaciones[x][i-lista_monedas[x][0]]),combinaciones[x][i])
                #print(combinaciones)
            else:
                combinaciones[x+1][i]=combinaciones[x][i]
    print(combinaciones)
    return combinaciones

def main():
    peso= stdin.readline().strip()
    while peso != "":
        casos=int(stdin.readline().strip())
        lista=[]
        for x in range(casos):
            a,b=stdin.readline().strip().split()
            lista.append([int(a),int(b)])
        lis = cambio(int(peso)+1,lista)
        print(lis[-1][-1])
        #if imprime == 1 :
#            print("There is only 1 way to produce "+str(a)+" cents change.")
#        else:
#            print("There are "+str(imprime)+" ways to produce "+str(a)+" cents change.")
        peso= stdin.readline().strip()
main()
