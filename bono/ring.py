from sys import stdin

def solucion(a):
    if(n == 1):
        print(n)

    elif len(a) == n:
        if a[0] + a[-1] in primos:
            print (*a)

    else:
        for i in range(2, n+1):
            if i not in r and ((a[-1]+i) in primos):
                if i in (a):
                    break
                else:
                    r.add(i)
                    solucion(a + [i])
                    r.remove(i)

def main():
    global n
    global primos
    global r
    n = stdin.readline().strip()
    ct = 1
    while (n != ''):
        print('Case '+str(ct)+':')
        n = int(n)
        primos = set([3,5,7,11,13,17,19,23,29,31,37])
        a = [1]
        r = set()
        solucion(a)
        n = stdin.readline().strip()
        ct= ct+1
main()

