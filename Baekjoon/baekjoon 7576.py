import sys

inp=sys.stdin.readlines()

m,n=map(int,inp[0].split())
tomatoes=[]
for i in range(n):
    tomatoes.append(list(map(int,inp[i+1].split())))
num=-1
frontier=[]

dx=[0,0,1,-1]
dy=[1,-1,0,0]
#starting point finding

for i in range(n):
    for j in range(m):
        if tomatoes[i][j]==1:
            frontier.append([i,j])



while frontier:
    next=[]
    num+=1
    for u in frontier:

        for k in range(4):
            x=dx[k]
            y=dy[k]
            if 0<=(u[0]+y) and (u[0]+y)<n and 0<=(u[1]+x) and (u[1]+x)<m and tomatoes[u[0]+y][u[1]+x]==0:
                next.append([u[0]+y,u[1]+x])

                tomatoes[u[0] + y][u[1] + x]=1
    frontier=next
if [0] in tomatoes:
    print(-1)
else:
    if num==-1:
        print(0)
    else:
        print(num)

