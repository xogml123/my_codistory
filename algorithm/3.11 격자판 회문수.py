nums=[]
result=0
for i in range(7):
    nums.append(list(map(int,input().split())))
for i in range(3):
    for j in range(7):
        temp=[]
        for k in range(5):
            temp.append(nums[i+k][j])
        temp1=temp.copy()
        temp.reverse()
        if temp==temp1:
            result+=1
for i in range(7):
    for j in range(3):
        temp=nums[i][j:j+5]
        temp1=temp.copy()
        temp.reverse()
        if temp==temp1:
            result+=1

print(result)


