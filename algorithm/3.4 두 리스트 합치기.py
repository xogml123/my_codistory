n=int(input())
numList1=list(map(int,input().split()))
m=int(input())
numList2=list(map(int,input().split()))
i=0
j=0
result=[]
while True:
    if i==n and j!=m:
        result.extend(numList2[j:])
        break
    elif i!=n and j==m:
        result.extend(numList1[i:])
        break
    else:
        if numList1[i]>numList2[j]:
            result.append(numList2[j])
            j+=1
        else:
            result.append(numList1[i])
            i+=1
for num in result:
    print(num,end=' ')
