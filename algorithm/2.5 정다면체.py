n,m=map(int,input().split())

n_num=[i+1 for i in range(n)]
m_num=[i+1 for i in range(m)]
sums={}
for i in range(len(n_num)):
    for j in range(len(m_num)):
        sum=n_num[i]+m_num[j]

        if sum not in sums:
            sums[sum]=1
        else:
            sums[sum]+=1
sums_values=list(sums.values())
maxv=max(sums_values)

for key in sums:
    if sums[key]==maxv:
        print(key,end=' ')
