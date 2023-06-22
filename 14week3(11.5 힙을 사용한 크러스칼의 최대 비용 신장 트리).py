vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [None,	29,		None,	None,	None,   10,		None],
           [29,	None,	16,		None,	None,	None,	15  ],
           [None,	16,		None,	12,		None,	None,	None],
           [None,	None,   12,		None,	22,		None,	18  ],
           [None,	None,	None,   22,		None,	27,		25  ],
           [10,	None,	None,	None,   27,		None,	None],
           [None,  15,		None,   18,		25,		None,	None]]

class MaxHeap :
    def __init__ (self) :
        self.heap = []
        self.heap.append(0)

    def size(self) : return len(self.heap) - 1
    def isEmpty(self) : return self.size() == 0
    def Parent(self, i) : return self.heap[i//2]
    def Left(self, i) : return self.heap[i*2]
    def Right(self, i) : return self.heap[i*2+1]
    def display(self, msg = '힙 트리: ') :
        print(msg, self.heap[1:])

    def insert(self, n) :
        self.heap.append(n)
        i = self.size()
        while (i != 1 and n.key > self.Parent(i).key):
            self.heap[i] = self.Parent(i)
            i = i // 2
        self.heap[i] = n

    def delete(self) :
        parent = 1
        child = 2
        if not self.isEmpty() :
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while (child <= self.size()):
                if child<self.size() and self.Left(parent).key<self.Right(parent).key:
                    child += 1
                if last.key >= self.heap[child].key :
                    break;
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2;

            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot

class HNode:
    def __init__(self, v1,v2, key):
        self.key=key
        self.v1=v1
        self.v2=v2

    def __lt__(self, other):
        return self.key<other.key

    def __le__(self, other):
        return self.key<=other.key


parent = []
set_size = 0

def init_set(nSets) :
    global set_size, parent
    set_size = nSets;
    for i in range(nSets):
        parent.append(-1)

def find(id) :
    while (parent[id] >= 0) :
        id = parent[id]
    return id;

def union(s1, s2) :
    global set_size
    parent[s1] = s2
    set_size = set_size - 1

def MaxSTKruskal(vertex, adj):
    vsize = len(vertex)
    init_set(vsize)
    eList = MaxHeap()
    sum=0
    for i in range(vsize-1) :
        for j in range(i+1, vsize) :
            if adj[i][j] != None :
                eList.insert( HNode(i,j,adj[i][j]) )



    edgeAccepted = 0
    while (edgeAccepted < vsize - 1) :
        e = eList.delete()
        uset = find(e.v1)
        vset = find(e.v2)

        if uset != vset :
            print("간선 추가 : (%s, %s, %d)" %
				(vertex[e.v1], vertex[e.v2], e.key))
            sum+=e.key
            union(uset, vset)
            edgeAccepted += 1
    return sum

print("MaxST By Kruskal's Algorithm")
print("MaxST 가중치의 합 = ",MaxSTKruskal(vertex, weight))