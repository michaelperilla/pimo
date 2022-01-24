#Tomando que el grafo es un diccionario
import heapq
from collections import deque
INF = float("INF")

####################################################################################
def dij_relax(u,v,w):
    global Q,dis,pad

    if dis[v]>dis[u]+w:     #si se mejora la distancia se actualiza
        dis[v] = dis[u] + w
        pad[v] = u         #ahora el antecesor de v es u
        heapq.heappush(Q,(dis[v],v)) #se introduce al heap con mejor distancia


def Dijkstra(grafo,s):
    global INF,Q,dis,pad

    # cantidad de vertices en el grafo "n"
    dis = [INF]* n
    pad = [None]* n

    dis[s] = 0 #distancia del vertice inicial es 0
    
    Q = []
    heapq.heappush(Q,(dis[s],s)) # colocar en el heap la distancia del vertice

    while Q:
        d,u = heapq.heappop(Q)
        for tup in grafo[u]: #para v en los vecinos de u, con sus pesos (v,peso)
            v = tup[0]
            w = tup[1] #donde w es el peso de ir de u a v
            dij_relax(u,v,w)

    return dis

####################################################################################        
def bell_relax(u,v,w):
    global dis,pad

    if dis[v] > dis[u] + w:
        dis[v] = dis[u]+w
        pad[v] = u
    
def Bellman_Ford(grafo,s):
    global INF,dis,pad

    dis = [INF]*n #cantidad de vertices en el grafo "n"
    pad = [None]*n
    
    dis[s] = 0 #distancia vertice de salida = 0


    for i in range(n-1): #en el rango de n-1 vertices
        for u in grafo: #para cada vertice u en el grafo
            for tup in grafo[u]: #para cada vecino de u
                v = tup[0]
                w = tup[1]
                bell_relax(u,v,w)


    for u in grafo:   #para cada vertice u
        for tup in grafo[u]:#para cada vecino de u
            v = tup[0]
            w = tup[1]
            if dis[v]>dis[u]+w: #verificar si hay ciclo negativo
                return "Ciclo Negativo"
    return "Sin Ciclo Negativo"       
######################################################################################

def make_set(v):
    global pad,ran
    pad[v],ran[v] = v,0

def find(v):
    global pad
    if v == pad[v]:
        return v
    else:
        pad[v] = find(pad[v])
        return pad[v]

def union(v1,v2):
    global pad,dis
    
    rv1 = find(v1)
    rv2 = find(v2)

    if rv1 != rv2:
        if ran[rv1] < ran[rv2]:
            pad[rv1] = rv2
        else:
            pad[rv2] = rv1
            if ran[rv1] == ran[rv2]:
                ran[rv1] += 1
        

def Kruskal(grafo):
    global pad,ran
    
    ran = dict()
    pad = dict()

    
    A = set()
    for v in grafo:          #para cada vertice. Hacer un make set
        make_set(v)
    
    #es posible sacar los arcos con una funcion auxiliar dependiendo del problema
    
    for edge in edges: #para cada arco
        #edge = (dis,v1,v2)
        dis,vertice1,vertice2 = edge[0],edge[1],edge[2]
        if find(vertice1) != find(vertice2):
            A.add(dis)
            union(vertice1,vertice2)
    return A
################################################################################################
#sea c la matriz de costos en donde i y j son vertices y c[i][j] es el costo de ir de uno a otro
c = [[0, 3, 8, INF, -4],
     [INF, 0, INF, 1, 7],
     [INF, 4, 0, INF, INF],
     [2, INF, -5, 0, INF],
     [INF, INF, INF, 6, 0]
    ]

#n es la cantidad de vertices, en este caso son 5

def Floyd_Warshall(c,n): #all_pairs algoritmo
    fw = [[0]*n for i in range(N)]
    for i in range(n):
        for j in range(n):
            fw[i][j] = c[i][j]    # se copia los costos en otra matriz para poder realizar floydwarshall

    #este es el algoritmo
    for k in range(n):
        for i in range(n):
            for j in range(n):
                fw[i][j] = min(fw[i][j],fw[i][k]+fw[k][j])
    return fw # la matriz con la menor distancia entre todas la parejas del grafo
    
################################################################################################
def bfs(grafo,s):
    global INF
    
    color = ["WHITE"]*n #n cantidad de vertices
    dis = [INF]*n
    pad = [None]*n

    #color del vertice inicial, gris, visitado pero no procesado
    color[s] = "GRAY"
    dis[s] = 0 #distancia es 0 del vertice inicial

    Q = deque() #cola
    Q.append(s) #insertar al vertice inicial en la cola

    while Q: #mientras la cola no este vacia
        u = Q.popleft()#sacar primer elemento
        for v in grafo[u]: #para cada vecino v de u
            if color[v]=="WHITE": #significando que no se a visitado
                color[v] = "GRIS" #procesando vertice
                dis[v] = dis[u] + 1
                pad[v] = u
                Q.append(v)
        color[u] = "BLACK" #se completo su procesamiento

    return dis
#############################################################################################

def dfs_visit(grafo,u):
    global time,pad,color,dis_i,dis_f
    time += 1
    dis_i[u] = time
    color[u] = "GRAY"

    for v in grafo[u]: #para cada vecino v de u
        if color[v]=="WHITE":#si no se a visto ese vertice
            pad[v] = u
            dfs_visit(grafo,v)
            
    color[u]= "BLACK"
    time += 1 
    dis_f[u] = time
    

        
def dfs(grafo):
    global color,pad,time,dis_i,dis_f

    color = ["WHITE"]*n #n cantidad de vertices
    pad = [None]*n
    dis_i = [None]*n
    dis_f = [None]*n

    
    time = 0
    for u in grafo:#para cada vertice u en el grafo
        if color[u]=="WHITE": #si no se a visto
            dfs_visit(grafo,u)
################################################################################################
def topological_sort(grafo):
    global stack
    
    stack = deque() #la funcion crea un stack
    dfs_top(grafo) #desde esta se llama al dfs
    return stack

def dfs_top(grafo):
    global color,dis
    
    for u in grafo:
        color[u] = "WHITE"
        padre[u] = None

    time = 0
    for u in grafo:
        if color[u]=="WHITE":
            dfs_visit_top(grafo,u,time)


def dfs_visit_top(grafo,u,time):
    global dis,padre,color,dis_f,stack
    
    time = time + 1
    dis[u] = time
    color[u] = "GRAY"
    for v in grafo[u]:
        if color[v] == "WHITE":
            padre[v] = u
            dfs_visit_top(grafo,v,time)
    color[u] = "BLACK"
    
    stack.appendleft(u)   #####Stack del topological_sort, coloca el vertice "u" a la izquierda en el arreglo
                          #####Luego de haberlo procesado en el dfs.
    
    time = time + 1
    dis_f[u] = time
#####################################################################################################
def prim():
    global vertices, adj
    tree = set()
    initial = vertices[0]
    tree.add(initial)
    PQ = []
    weight  = {}
    par = {}
    for v in vertices:
        weight[v] = float("inf")
        par[v] = None
    # weight[v]: es el peso mínimo de un arco que atraviesa
    # el corte (u, v) en donde u esta en T y v en C-T.
    for t in adj[initial]:
        w = t[1]
        v = t[0]
        heappush(PQ, (w, v))
        weight[v] = w
        par[v] = initial
    #print(weight)
    total_weight = 0
    edges = []
    while len(tree)!=len(vertices):
        t = heappop(PQ)
        w, v = t
        if not v in tree:
            tree.add(v)
            total_weight += w
            edges.append((v, par[v]))
            for x in adj[v]:
                wu, u = x[1], x[0]
                if weight[u] > wu:
                    weight[u] = wu
                    par[u] = v
                    heappush(PQ, (wu, u))
    print(edges)
    return total_weight
    
vertices = ['a','b','c','d','e','f','g','h','i']
adj = {}
adj['a'] = [('b', 4), ('h', 8)]
adj['b'] = [('a', 4), ('h', 11), ('c', 8)]
adj['c'] = [('b', 8), ('i', 2), ('f', 4), ('d', 7)]
adj['d'] = [('c', 7), ('f', 14), ('e', 9)]
adj['e'] = [('d', 9), ('f', 10)]
adj['f'] = [('d', 14), ('c', 4), ('g', 2), ('e', 10)]
adj['g'] = [('f', 2), ('i', 6), ('h', 1)]
adj['h'] = [('g', 1), ('i', 7), ('b', 11), ('a', 8)]
adj['i'] = [('h', 7), ('g', 6), ('c', 2)]
print(prim())
    

########################################################################################

