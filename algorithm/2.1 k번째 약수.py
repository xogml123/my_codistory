n,k=map(int,input().split())
nums=[]
for dvder in range(1,n+1):
    q,r=map(int,divmod(n,dvder))

    if r==0:
        nums.append(dvder)
try:
    result=nums[k-1]
    print(result)
except:
    print(-1)

