from sys import stdin
def main():
    z = int(stdin.readline().strip())
    for i in range(z):
        ob,cofre=[int (_) for _ in  stdin.readline().strip().split()]
        valores = [int (_) for _ in  stdin.readline().strip().split()]
        peso = [int (_) for _ in  stdin.readline().strip().split()]
        matriz = [[0 for i in range(cofre+1)]for j in range(ob+1)]
        for i in range(ob+1):
            for j in range(cofre+1):
                if j == 0 or i == 0:
                    matriz[i][j] =  0
                    continue
                elif j - peso[i-1] < 0 :
                    matriz[i][j] =  matriz[i-1][j]
                else:
                    matriz[i][j] = max(matriz[i-1][j],valores[i-1]+matriz[i-1][j-peso[i-1]])
        print(matriz[-1][-1])
    
main()
 
