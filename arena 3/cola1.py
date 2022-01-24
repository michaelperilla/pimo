from sys import stdin
from math import ceil as cielo
from math import log2
from bisect import bisect_right
def main():
    cases = int(stdin.readline().strip())
    for i in range(cases):
        num = int(stdin.readline().strip())
        array = list(map(int,stdin.readline().strip().split()))
        arr = []
        conta = 0
        for j in range(len(array)):
            if array[j] != 0:
                pos = bisect_right(arr,array[j])
                arr.insert(pos,array[j])
                conta += cielo(log2(len(arr)))+len(arr[pos+1:])+1
               
            else:
                arr.remove(arr[-1])
                conta += 1
        print(conta)
            
        
main()
