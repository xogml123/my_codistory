n,m=map(int,input().split())
A=[-1]
A.extend(list(map(int,input().split())))
result=0
index=0
for i in range(1,n+1):
    if index==0:
        for j in range(i,n+1):
            temp=sum(A[i:j+1])
            if temp<m:
                continue
            elif temp==m:
                result+=1
                index=j+1
                break
            else:
                index=j
                break
    elif index!=0:
        for j in range(index,n+1):
            temp = sum(A[i:j + 1])
            if temp < m:
                continue
            elif temp == m:
                result += 1
                index=j+1
                break
            else:
                index = j
                break
print(result)


