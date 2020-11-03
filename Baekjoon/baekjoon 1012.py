import sys

inp=sys.stdin.readlines()

t=int(inp[0].strip('\n'))
s=2
p=1
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bfs(start,testcase):
    frontier=[]
    frontier.append(start)
    visited.append(start)
    while frontier:
        temp=[]
        for fron in frontier:

            for i in range(4):
                if [fron[0]+dx[i],fron[1]+dy[i]] not in visited and 0<=(fron[0]+dx[i]) and (fron[0]+dx[i])<m and 0<=(fron[1]+dy[i]) and (fron[1]+dy[i])<n and testcase[fron[1]+dy[i]][fron[0]+dx[i]]==1:
                    temp.append([fron[0]+dx[i],fron[1]+dy[i]])
                    visited.append([fron[0]+dx[i],fron[1]+dy[i]])
        frontier=temp



for i in range(t):
    m, n, k = map(int, inp[p].split())
    testcase=[[0]*m for l in range(n)]
    worm=0
    visited=[]

    for j in range(k):
        temp=list(map(int,inp[s+j].split()))
        testcase[temp[1]][temp[0]]=1
    for x in range(m):
        for y in range(n):
            if testcase[y][x]==1 and [x,y] not in visited:
                bfs([x,y],testcase)
                worm+=1
    print(worm)
    s+=k+1
    p+=k+1




