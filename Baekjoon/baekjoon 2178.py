import sys

inp=sys.stdin.readlines()
n,m=list(map(int,inp[0].split()))
new_inp=[]
for i in range(1,len(inp)):
    new_inp.append(list(inp[i].strip()))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

queue=[[0,0]]
new_inp[0][0]=1

while queue:
    a,b=queue[0][0],queue[0][1]
    del queue[0]
    for i in range(4):
        x=a+dx[i]
        y=b+dy[i]
        if 0<=x<n and 0<=y<m and new_inp[x][y]=='1':
            queue.append([x,y])
            new_inp[x][y]=new_inp[a][b]+1

print(new_inp[n-1][m-1])
 


    

