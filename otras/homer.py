from sys import stdin
import sys
sys.setrecursionlimit(1000000)

def hambu(t):
    global m,n,memo
    if(t <= 0):
        return 0
    elif(m > t and n > t):
        return -1
    elif (t >= m and t < n):
        return 1+hambu(t-m)
    elif(t > n and t < m):
        return 1+hambu(t-n)
    elif memo[t]!=-1:
        return memo[t]
    else:
        memo[t]=max (1+hambu(t-n),1+hambu(t-m))
        return memo[t]

def main():
    global m, n,memo
    lista = [int(i) for i in stdin.readline().strip().split()]
    while lista:
        m=lista[0]
        n=lista[1]
        t=lista[2]
        memo=[-1 for i in range(t+1)]
        print(memo)
        print(hambu(t))
        lista = [int(i) for i in stdin.readline().strip().split()]
            
main()
