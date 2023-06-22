def st_dfs_recur(adj, vtx,visited, id):
    visited[id] = True
    for i in range(len(vtx)):
        if adj[id][i] == 1:
            if visited[i] is not True:
                print("(",vtx[id],",",vtx[i],")", end=' ')
                st_dfs_recur(adj, vtx, visited, i)
    return

def st_dfs(adj, vtx, s):
    n=len(vtx)
    visited=[False]*n
    st_dfs_recur(adj, vtx, visited, s)
    return
vertex = ['A','B','C','D','E','F','G','H']
adjMat = [[0,1,1,0,0,0,0,0],
          [1,0,0,1,0,0,0,0],
          [1,0,0,1,1,0,0,0],
          [0,1,1,0,0,1,0,0],
          [0,0,1,0,0,0,1,1],
          [0,0,0,1,0,0,0,0],
          [0,0,0,0,1,0,0,1],
          [0,0,0,0,1,0,1,0]]
print('Spanning Tree(DFS) : ',end='')
st_dfs(adjMat,vertex,0)
print()