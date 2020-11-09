n=int(input())
qubics=[]
rewards=[]
for i in range(n):
    qubics.append(list(map(int,input().split())))
for qubic in qubics:
    nums={1:0,2:0,3:0,4:0,5:0,6:0}
    for num in qubic:
        nums[num]+=1
    alldiff = []
    for key in nums:
        if nums[key]==3:
            rewards.append(10000+key*1000)
        elif nums[key]==2:
            rewards.append(1000+key*100)
        else:
            alldiff.append(key)
    rewards.append(max(alldiff)*100)
print(max(rewards))
