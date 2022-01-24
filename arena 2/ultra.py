from sys import stdin


def mergeSort(alist):
    global cont
    if len(alist)>1:
        i=0
        j=0
        k=0
        mid = len(alist)//2
        lefthalf = alist[:mid]
        mergeSort(lefthalf)
        righthalf = alist[mid:]
        mergeSort(righthalf)
        
        while len(lefthalf) > i  and len(righthalf) > j :
            if righthalf[j] > lefthalf[i] :
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                cont+=len(lefthalf)-i
                j=j+1
            k=k+1
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
    
def main():
    global cont
    n = int(stdin.readline())
    while (n != 0):
        cont = 0
        lista = []
        for x in range(n):
            lista.append(int(stdin.readline()))
        mergeSort(lista)
        print(cont)
        n=int(stdin.readline())
main()
