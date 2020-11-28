n=int(input())
taller=list(map(int,input().split()))
max_num=10*5
people=[max_num]*n

for i in range(n):
    j=0
    index=0
    while j<=taller[i]:
        if people[index]==max_num and j==taller[i]:
            break
        elif people[index]==max_num:
            j+=1
            index+=1
        elif people[index]!=max_num:
            j+=0
            index+=1
    people[index]=i+1
    
for i in range(n):
    print(people[i],end=' ')
    
            
    