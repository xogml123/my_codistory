import sys

inp=sys.stdin.readlines()

n=int(inp[0].strip('\n'))
m=int(inp[1].strip('\n'))


adj={}
for i in range(m):
    temp=list(inp[i+2].split())
    if temp[0] not in adj:
        adj[temp[0]]=[temp[1]]
    else:
        adj[temp[0]].append(temp[1])
    if temp[1] not in adj:
        adj[temp[1]]=[temp[0]]
    else:
        adj[temp[1]].append(temp[0])

def bfs(adj,start):
    num=-1
    visited=[]
    frontier=[]
    frontier.append(start)
    visited.append(start)
    while frontier:
        temp=[]
        for computer in frontier:

            num += 1

            for fron in adj[computer]:
                if fron not in visited:
                    visited.append(fron)
                    temp.append(fron)
        frontier=temp
    return num

print(bfs(adj,'1'))





