def topological_sort(graph):
    inDeg={}
    for i in graph.keys():
        inDeg.setdefault(i,0)
    for i in graph.keys():
        for j in graph.get(i):
            inDeg[j]+=1
    vlist=[]
    for i in inDeg.keys():
        if inDeg[i]==0:
            vlist.append(i)
    while len(vlist)>0:
        v=vlist.pop()
        print(v, end=' ')
        for i in graph.get(v):
            for j in inDeg.keys():
                if i==j:
                    inDeg[j]-=1
                    if inDeg[j]==0:
                        vlist.append(j)


mygraph={'A':set(['C','D']),
         'B':set(['D','E']),
         'C':set(['D','F']),
         'D':set(['F']),
         'E':set(['F']),
         'F':set([])}

print('topological_sort: ')
topological_sort(mygraph)
print()