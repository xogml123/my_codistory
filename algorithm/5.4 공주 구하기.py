n,k=map(int,input().split())

princes=[i for i in range(1,n+1)]
index=-1
for i in range(n-1):
    temp=index
    index+=k
    if index%len(princes)> temp%len(princes):

    princes.pop(index%len(princes))
print(princes[0])


