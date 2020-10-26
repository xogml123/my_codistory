import sys

inp=sys.stdin.readlines()

n=int(inp[0].strip('\n'))

ballons=list(map(int,inp[1].split()))
result=0

while ballons:
    j=0
    m=max(ballons)

    while len(ballons)-1 >= j:
        if ballons[j]==m:
            ballons[j]=-1
            j+=1
            m-=1
        elif ballons[j]!=m:
            j+=1
            continue

    result+=1
#시간초과


