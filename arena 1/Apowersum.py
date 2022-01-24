from sys import stdin
def powerSum(n,x,num):
    cot = num**x
    if cot == n:
        return 1
    elif cot > n:
        return 0
    else:
        return powerSum(n,x,num+1)+powerSum(n-cot,x,num+1)

def main():
    n = stdin.readline()
    while n != "":
        n = int(n)
        x = int(stdin.readline().strip())
        print(powerSum(n,x,1))
        n = stdin.readline()
main()
