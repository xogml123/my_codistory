import sys
import copy
inp=sys.stdin.readlines()

n,m=map(int,inp[0].split())
mapv=[]
results=[]
for i in range(n):
    mapv.append(list(map(int,inp[i+1].split())))

dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bfs(start,mapv):
    frontier=[]
    frontier.append(start)
    visited.append(start)
    while frontier:
        temp=[]
        for fron in frontier:
            x=fron[1]
            y=fron[0]

            for i in range(4):
                x_=x+dx[i]
                y_=y+dy[i]
                if 0<=y_ and y_<n and 0<=x_ and x_<m and mapv[y_][x_]==0:
                    temp.append([y_,x_])
                    visited.append([y_,x_])
                    mapv[y_][x_]=2
        frontier=temp

zeros=[]
cases=[]
for i in range(n):
    for j in range(m):
        if mapv[i][j]==0:
            zeros.append([i,j])
for i in range(len(zeros)-2):
    for j in range(i+1,len(zeros)-1):
        for k in range(j+1,len(zeros)):
            temp=[zeros[i],zeros[j],zeros[k]]
            cases.append(temp)
for case in cases:
    result=0
    mapvc=copy.deepcopy(mapv)
    visited=[]
    for g in range(3):
        mapvc[case[g][0]][case[g][1]]=1

    for i in range(n):
        for j in range(m):
            if mapvc[i][j] == 2 and [i,j] not in visited:
                bfs([i, j], mapvc)
    for i in range(n):
        for j in range(m):
             if mapvc[i][j] == 0:
                result += 1
    results.append(result)

print(max(results))








