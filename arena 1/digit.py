from sys import stdin

def suma(lista):
    sum(map(int,lista))

if (len(lista)<2):
    suma(print(lista))

else:
    suma(lista)


def main():
    lista = []
    x,x1 = (stdin.readline().strip().split(" "))
    x = str(x)
    x1 = int(x1)

    for i in range(x1):
        lista.append(x)
    print(suma(lista))

    lista = "".join(lista)
main()
