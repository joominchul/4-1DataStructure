import sys
sys.setrecursionlimit(10**8)
def hash(k):
    return k%11
##선형조사법
def add(map,n,i):
    if n==11:
        n=0
    if map[n]==0:
        map[n]=i
    else:
        add(map,n+1,i)
list=[12,44,13,88,23,94,11,39,20,16,5]
map=[0,0,0,0,0,0,0,0,0,0,0]

for i in list:
    n=hash(i)
    print(i,":",n,end='/')
    add(map,n,i)
print()
print(map)

map=[0,0,0,0,0,0,0,0,0,0,0]
#이차조사법
def qua(k,i):
    return (hash(k)+(i*i))%11
ii=0

for i in list:
    n=qua(i,ii)
    ii=ii+1
    print(i,":",n,end=' ')
    add(map,n,i)
print()
print(map)

#이중 해시
map=[0,0,0,0,0,0,0,0,0,0,0]
def double(j):
    return 7-(j%7)
def add1(map,n,i):
    if n==11:
        n=0
    if map[n]==0:
        map[n]=i
    elif map[double(n)]==0:
        map[double(n)]=i
    else:
        add(map,double(n)+1,i)
for i in list:
    n=hash(i)
    print(i,":",n,end='/')
    add1(map,n,i)
print()
print(map)