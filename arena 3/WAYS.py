from sys import stdin
def main():
    global M
    M=[1,5,10,25,50]
    global matriz
    matriz=[[0 for i in range(len(M)+1)]for j in range(30001)]


    for m in range(len(matriz)):
        for i in range(len(matriz[m])):
            if m==0:
                matriz[m][i] = 1
            elif i==0:
                matriz[m][i] = 0
            
            elif  m < M[i-1]:
                matriz[m][i] = matriz[m][i-1]
            else:
                matriz[m][i] = matriz[m-M[i-1]][i]+ matriz[m][i-1]
    while(True):
        a=stdin.readline().strip()
        if a=='':
            break
        else:
            a=int(a)
            if matriz[a][5] == 1:
                print('There is only',matriz[a][5],'way to produce',a,'cents change.')
            else:
                print('There are',matriz[a][5],'ways to produce',a,'cents change.')
main()
