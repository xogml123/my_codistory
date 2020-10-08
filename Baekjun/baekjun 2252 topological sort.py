import sys
n,m=map(int,input().split())
if n==1:
    print(1)
    a=input()
else:
    edges=[]
    vertices={}
    for i in range(m):
        edges.append(sys.stdin.readline().split())
    for i in range(1,n+1):
        num=0
        for edge in edges:
            if edge[1]==str(i):
                num+=1
        vertices[str(i)]=num

    def topo_sort(vertices,edges):
        q=[]
        while vertices:
            temp=[]
            for vertice in vertices:

                if vertices[vertice]==0:
                    temp.append(vertice)

            q.extend(temp)
            rem=[]
            for vertice in vertices:
                if vertices[vertice]==0:
                    rem.append(vertice)
            for r in rem:
                del vertices[r]

            for edge in edges:
                if edge[0] in temp:
                    vertices[edge[1]]-=1
            rem=[]
            for edge in edges:
                if edge[0] in temp:
                    rem.append(edge)
            for i in range(len(rem)):
                edges.remove(rem[i])

        return q
    queue=topo_sort(vertices,edges)
    for qu in queue:
        print(qu,end=' ')

