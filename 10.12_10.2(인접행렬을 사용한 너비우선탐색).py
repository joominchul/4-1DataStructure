import collections

def bfs(a,ver, start):
    n = len(ver)
    visited = [False] * n
    queue = collections.deque([start])
    visited[start] = True
    while queue:                        
        vertex = queue.popleft()        
        print(ver[vertex], end=' ')
        for v in range(n):
            if a[vertex][v]==1:
                if visited[v] is not True:
                    visited[v]=True
                    queue.append(v)

v=['0','1','2','3','4','5','6','7','8','9']
a=[[0,1,0,0,0,0,0,0,0,0],
   [1,0,1,1,0,0,0,0,0,0],
   [0,1,0,0,1,0,0,0,0,0],
   [0,1,0,0,1,1,0,0,0,0],
   [0,0,1,1,0,0,0,0,0,0],
   [0,0,0,1,0,0,1,1,0,0],
   [0,0,0,0,0,1,0,1,0,0],
   [0,0,0,0,0,1,1,0,1,1],
   [0,0,0,0,0,0,0,1,0,0],
   [0,0,0,0,0,0,0,1,0,0]]

bfs(a,v,3)