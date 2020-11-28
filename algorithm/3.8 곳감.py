n=int(input())
gams=[]
for i in range(n):
    gams.append(list(map(int,input().split())))
m=int(input())
insts=[]
for i in range(m):
    insts.append(list(map(int,input().split())))

def rota(inst,gams):
    temp=[None for i in range(n)]
    if inst[1]==0:
        for j in range(n):
            temp[(j-inst[2])%n]=gams[inst[0]-1][j]
    else:
        for j in range(n):
            temp[(j+inst[2])%n]=gams[inst[0]-1][j]
    gams[inst[0]-1]=temp
#rotation 하기
for inst in insts:
    rota(inst,gams)
#합구하기
subs=0
sums=0
for i in range(1,n-1):
    for j in range(0,n//2-abs(n//2-i)):
        subs+=gams[i][j]
    for j in range(n//2+1+abs(n//2-i),n):
        subs+=gams[i][j]

for i in range(n):
    sums+=sum(gams[i])
print(sums-subs)



