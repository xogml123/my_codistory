n=int(input())
sums=[]

nums=[]
for i in range(n):
    nums.append(list(map(int,input().split())))

for i in range(n):
    sums.append(sum(nums[i]))
for j in range(n):
    temp=[]
    for i in range(n):

        temp.append(nums[i][j])
    sums.append(sum(temp))
temp=[]
for i in range(n):
    temp.append(nums[i][i])
sums.append(sum(temp))
temp=[]
for i in range(n):
    temp.append(nums[i][n-i-1])
sums.append(sum(temp))
print(max(sums))