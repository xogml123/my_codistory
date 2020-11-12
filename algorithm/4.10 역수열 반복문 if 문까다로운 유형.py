n=int(input())
re_sequence=list(map(int,input().split()))
sequence=[0 for i in range(n)]
for i in range(n):
    j=0
    bigger=0
    while True:
        if bigger>re_sequence[i]:
            j-=1
            break
        else:
            if sequence[j]==0:
                bigger+=1
                j+=1
            else:
                j+=1
    sequence[j]=i+1

for se in sequence:
    print(se,end=' ')

