n=int(input())
mapping=[]
mapping.append([0]*(n+2))
for i in range(n):
    mapping.append([0]+list(map(int,input().split()))+[0])
mapping.append([0]*(n+2))
di=[0,0,-1,1]
dj=[1,-1,0,0]
result=0
for i in range(1,n+1):
    for j in range(1,n+1):
        index=0
        for k in range(4):
            i_=i+di[k]
            j_=j+dj[k]
            if mapping[i_][j_]>=mapping[i][j]:
                index=1
                break
            else:
                continue
        if index==0:
            result+=1
print(result)



