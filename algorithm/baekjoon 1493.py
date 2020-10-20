import sys
inp=sys.stdin.readlines()

l,w,h=map(int,inp[0].split())
n=int(inp[1].strip('\n'))
cubes=[]
for i in range(n):
    temp=list(map(int,inp[i+2].split()))

    cubes.append([2**temp[0],temp[1]])
cubes.reverse()

for cube in cubes:
    if cube[0]<=l and


