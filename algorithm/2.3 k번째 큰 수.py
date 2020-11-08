n,k=map(int,input().split())
nums=[]
adds=[]
nums.extend(list(map(int,input().split())))

for i in range(n-2):
    for j in range(i+1,n-1):
        for l in range(j+1,n):
            adds.append(nums[i]+nums[j]+nums[l])
adds.append(10000)
adds.sort(reverse=True)
i=0
index=0
while index<k:
    i += 1
    if adds[i]==adds[i-1]:
        pass
    else:
        index+=1

print(adds[i])

