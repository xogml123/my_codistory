n,c=map(int,input().split())
hhs=[]
for i in range(n):
    hhs.append(int(input()))
hhs.sort()
distances=[]
for i in range(len(hhs)-1):
    distances.append(abs(hhs[i+1]-hhs[i]))


