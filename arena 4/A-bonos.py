from sys import stdin
def bonos_viaje(x,y,a):
    global lon,lista,memo,checked
    if x<0:
        memo[(x,y,a)]=0
        return memo[(x,y,a)]
    if (x,y,a) in memo:
        return memo[(x,y,a)]
    else:
        if y<=0 and a<=0:
            memo[(x,y,a)] = lista[x]+bonos_viaje(x-1,y,a)
            return memo[(x,y,a)]
        if y>0 and a<=0:
            memo[(x,y,a)]=min(bonos_viaje(x-3,y-1,a),lista[x]+bonos_viaje(x-1,y,a))
            return memo[(x,y,a)]
        if y<=0 and a>0:
            memo[(x,y,a)]=min(bonos_viaje(x-5,y,a-1),lista[x]+bonos_viaje(x-1,y,a))
            return memo[(x,y,a)]
        else:
            memo[(x,y,a)]=min(bonos_viaje(x-3,y-1,a),bonos_viaje(x-5,y,a-1),lista[x]+bonos_viaje(x-1,y,a))
            return memo[(x,y,a)]
     
def main():
    global lon,lista,memo,checked
    z = stdin.readline()
    z = int(z)
    while z>0:
        memo = {}
        x,y,a=[int (j) for j in stdin.readline().strip().split()]
        lista= [int (j) for j in stdin.readline().strip().split()]
        z = z-1
        print(bonos_viaje(x-1,y,a))
main()

