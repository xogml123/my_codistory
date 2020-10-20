import sys

inp=sys.stdin.readlines()

n,k=map(int,inp[0].split())

exs=list(map(int,inp[1].split()))
exs.sort()

ak=0
result=0
for i in range(len(exs)):
    result+=ak*exs[i]
    if ak<=k-1:
        ak+=1
print(result)

