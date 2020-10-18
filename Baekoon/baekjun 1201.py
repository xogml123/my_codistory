import sys

n,m,k=map(int,sys.stdin.readline())
if m+k>n+1:
    print(-1)
else:

    result=[]
    for i in range(m,0):
        result.append(i)
    for i in range(m+1,m+k):
        result.append(i)