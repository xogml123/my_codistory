n,m=map(int,input().split())
comp=[]
adj={}
for i in range(m):
    comp.append(input().split())
for c in comp:
    if c[0] not in adj:
        adj[c[0]]=c[1]
    else:
        adj[c[0]].append(c[1])

def topo_sort(adj):
    q = []
    vertices = [i for i in range(1, n + 1)]
    while len(q)==n:
        temp=vertices.copy()
        for key in adj:
            for node in adj[key]:
                if node in temp:
                    temp.remove(node)
    q.extend(temp)
    for t in temp:
        vertices.remove(t)
        del adj[t]







