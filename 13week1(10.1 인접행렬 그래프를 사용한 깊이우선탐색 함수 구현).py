def dfs_recur(adj, vtx,visited, id):
    print(vtx[id], end=' ')
    visited[id] = True
    for i in range(len(vtx)):
        if adj[id][i] == 1:
            if visited[i] is not True:
                dfs_recur(adj, vtx, visited, i)
    return

def dfs(adj, vtx, start):
    n=len(vtx)
    visited=[False]*n
    dfs_recur(adj, vtx, visited, start)

vertex = ['A','B','C','D','E','F','G','H']
adjMat = [[0,1,1,0,0,0,0,0],
          [1,0,0,1,0,0,0,0],
          [1,0,0,1,1,0,0,0],
          [0,1,1,0,0,1,0,0],
          [0,0,1,0,0,0,1,1],
          [0,0,0,1,0,0,0,0],
          [0,0,0,0,1,0,0,1],
          [0,0,0,0,1,0,1,0]]
print('DFS : ', end="")
dfs(adjMat,vertex,0)
print()