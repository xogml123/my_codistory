n,m=map(int,input().split())
if n==1:
    print()
comp=[]
adj={}
for i in range(m):
    comp.append(input().split())
if n==1:
    print(comp[o][0])
else:
    for c in comp:
        if c[0] not in adj:
            adj[c[0]]=c[1]
        else:
            adj[c[0]].append(c[1])


    def topo_sort(adj):
        q = []
        vertices = ['{0}'.format(i) for i in range(1, n + 1)]
        while adj:
            temp=vertices.copy()
            for key in adj:
                for node in adj[key]:
                    try:
                        temp.remove(node)
                    except:
                        pass

            q.extend(temp)
            for t in temp:
                vertices.remove(t)
                del adj[t]
        if adj=={}:
            q.extend(vertices)
        return q
    queue=topo_sort(adj)
    for person in queue:
        print(person,end=' ')








