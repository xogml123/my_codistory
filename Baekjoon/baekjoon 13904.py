import sys


inp=sys.stdin.readlines()

n=int(inp[0].strip('\n'))
assignments=[]
temp=[]
for i in range(1,n+1):
    assignments.append(list(map(int,inp[i].split())))
    temp.append(assignments[i-1][0])

days=[k for k in range(0,max(temp)+1)]
result=0
assignments=sorted(assignments,key=lambda x:x[1],reverse=True)

for ass in assignments:
    for i in range(ass[0],0,-1):
        if days[i]!=0:
            result+=ass[1]
            days[i]=0
            break
print(result)



