n,m=map(int,input().split())

weights=list(map(int,input().split()))

weights.sort(reverse=True)
result=0
while sum(weights)!=0:
    for i in range(len(weights)):

        if weights[i]!=0:
            temp=0
            temp+=weights[i]
            weights[i]=0
            for j in range(i+1,len(weights)):
                if weights[j]!=0:
                    if temp+weights[j]<=m:
                        temp+=weights[j]
                        weights[j]=0
                    else:
                        continue
            result+=1
print(result)

