import sys

inp=sys.stdin.readlines()
n,m=map(int,inp[0].split())
comps=[]
students=[i+1 for i in range(n)]
for i in range(m):
    comps.append(list(map(int,inp[i+1].split())))

links={}
for comp in comps:
    if comp[1] not in links:
        links[comp[1]]=1
    else:
        links[comp[1]]+=1

for student in students:
    if student not in links:
        links[student]=0
result=[]
while list(links.values())!=[None]*n:
    temp=[]
    for link in links:
        if links[link]==0:
            temp.append(link)
            links[link]=None
    result.extend(temp)
    for t in temp:
        for comp in comps:
            if comp[0]==t:
                links[comp[1]]-=1
for r in result:
    print(r,end=' ')

















