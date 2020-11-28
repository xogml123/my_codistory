n=int(input())
result=0
people=[]
for i in range(n):
    people.append(list(map(int,input().split())))
people.sort(key=lambda x:x[0])

for i in range(n):
    index=0
    for j in range(i+1,n):
        if people[i][1]<people[j][1]:
            index=1
            break
    if index==0:
        result+=1
print(result)