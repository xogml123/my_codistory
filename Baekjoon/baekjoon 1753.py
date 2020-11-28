import sys
from queue import PriorityQueue
inf=sys.maxsize
a=sys.stdin.readlines()
v_num,e=map(int,a[0].split())
k=a[1].strip('\n')
edges=[]
for i in range(2,len(a)):

    u,v,w=a[i].split()
    w=int(w)
edges.append([u,v,w])

vertices=[str(i) for i in range(v_num)]
def min_key(dir):
    min=inf
    min_key
    for key in dir:
        if dir[key]<=min:
            min=dir[key]
            min_key=key

    return min_key
dir={}
def dijkstra(edges,vertices,k):

    s=[k]



    for vertice in vertices:
        if vertice==k:
            dir[vertice]=0
        else:
            dir[vertice]=inf
    while dir:
        temp=min_key(dir)
        del dir[temp]
        s.append(temp)
        for edge in edges:
            if edge[0]==temp:
                if dir[edge[1]]>edge[2]+dir[edge[0]]:
                    dir[edge[1]]=edge[2]+dir[edge[0]]

for key in dir:
    print(dir[key])







