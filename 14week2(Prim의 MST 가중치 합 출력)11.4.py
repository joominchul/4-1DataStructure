vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [None,	29,		None,	None,	None,   10,		None],
           [29,	None,	16,		None,	None,	None,	15  ],
           [None,	16,		None,	12,		None,	None,	None],
           [None,	None,   12,		None,	22,		None,	18  ],
           [None,	None,	None,   22,		None,	27,		25  ],
           [10,	None,	None,	None,   27,		None,	None],
           [None,  15,		None,   18,		25,		None,	None]]
INF = 9999
def getMinVertex(dist, selected) :
    minv = 0
    mindist = INF
    for v in range(len(dist)) :
        if not selected[v] and dist[v]<mindist :
            mindist = dist[v]
            minv = v
    return minv

def MSTPrim(vertex, adj) :
    vsize = len(vertex)
    dist = [INF] * vsize
    selected = [False] * vsize
    dist[0] = 0
    sum1=0
    for i in range(vsize) :
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=' ')

        for v in range(vsize) :
            if (adj[u][v] != None):
                sum1+=adj[u][v]
                if selected[v]==False and adj[u][v]< dist[v] :
                    dist[v] = adj[u][v]
    print()
    return sum1//2

print("MST By Prim's Algorithm")
print("MST 가중치의 합 = ",MSTPrim(vertex, weight))