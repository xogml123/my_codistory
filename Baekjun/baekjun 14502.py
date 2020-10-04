import sys

inp=sys.stdin.readlines()
picture=[]
n,m=map(int,inp[0].split())

for i in range(1,len(inp)):
    picture.append(inp[i].split())

dx=[1,-1,0,0]
dy=[0,0,-1,1]
zero=[]
two=[]

comb_3=[]
for i in range(n):
    for j in range(m):
        if picture[i][j]=='2':
            two.append([i,j])
        elif picture[i][j]=='0':
            zero.append([i,j])

for i in range(len(zero)-2):
    for j in range(i+1,len(zero)-1):
        for k in range(j+1,len(zero)):
            comb_3.append([zero[i],zero[j],zero[k]])
def dfs(picture,s):
    q=[s]
    while q:
          x,y=q.pop(0)
          for i in range(4):
            
            
            x+=dx[i]
            y+=dy[i]
            if (0<=x and x<m) and (0<=y and y<n) and picture[x][y]=='0':
                picture[x][y]='2'
                q.append([x,y])
            
    
        
            
counters=[]
for case in comb_3:
    temp=picture
    temp[case[0][0]][case[0][1]]='1'
    temp[case[1][0]][case[1][1]]='1'
    temp[case[2][0]][case[2][1]]='1'
    for virus in two:
        dfs(temp,virus)
    counter=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]=='0':
                counter+=1
    counters.append(counter)

print(max(counters))

            

    
            



