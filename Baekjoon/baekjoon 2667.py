import sys

inp=sys.stdin.readlines()

n=int(inp[0].strip('\n'))
smap=[]
for i in range(n):
    smap.append(list(map(int,list(inp[i+1].strip('\n')))))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
result=[]
visited=[]
def bfs(graph,i,j):
    frontier=[]
    frontier.append([i,j])
    visited.append([i,j])
    num=0
    while frontier:
        next=[]
        for u in frontier:
            num+=1

            for k in range(4):
                y=dy[k]
                x=dx[k]
                try:
                    if graph[u[0]+y][u[1]+x]==graph[i][j] and [u[0]+y,u[1]+x] not in visited and 0<=(u[0]+y) and (u[0]+y)<n and 0<=(u[1]+x) and (u[1]+x)<n:
                        next.append([u[0]+y,u[1]+x])
                        visited.append([u[0]+y,u[1]+x])
                except:
                    pass
        frontier=next
    return num
for i in range(n):
    for j in range(n):
        if smap[i][j]!=0 and [i,j] not in visited:
            temp=bfs(smap,i,j)
            result.append(temp)

result.sort()
print(len(result))
for r in result:
    print(r)
