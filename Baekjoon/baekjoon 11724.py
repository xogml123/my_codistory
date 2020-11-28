n,m=map(int,input().split())
adj={}
cc=0
def bfs(start,adj,cc):
    cc+=1
    frontier=[]
    frontier.append(start)
    visited.append(start)
    while frontier:
        t=[]
        for fron in frontier:
            if fron not in adj:
                return cc
            else:
                for next in adj[fron]:
                    if next not in visited:
                        visited.append(next)
                        t.append(next)
        frontier=t
    return cc

for i in range(m):
    temp=list(input().split())
    if temp[0] not in adj:
        adj[temp[0]]=[temp[1]]
    else:
        adj[temp[0]].append(temp[1])
    if temp[1] not in adj:
        adj[temp[1]] = [temp[0]]
    else:
        adj[temp[1]].append(temp[0])

visited=[]
for i in range(n):
    node=str(i+1)
    if node not in visited:
        cc=bfs(node,adj,cc)


print(cc)



