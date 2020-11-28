import sys

inp=sys.stdin.readlines()
n=int(inp[0].strip('\n'))
juyusos=[]
for i in range(1,n+1):
    juyusos.append(list(map(int,inp[i].split())))
dest, start_fuel=map(int,inp[n+1].split())
#greedy 적용 연료 양으로
def func(loc,fuel,visit):
    if loc+fuel>=dest:
        return visit
    elif juyusos==[]:
        return -1
    else:
        avail=[]
        comp=[]
        after=[]
        for i in range(len(juyusos)):
            if abs(loc-juyusos[i][0])<=fuel:
                avail.append(juyusos[i])
        for juyu in avail:
            t1 = loc
            t2 = fuel
            t1=juyu[0]
            t2=fuel-abs(juyu[0]-loc)+juyu[1]
            comp.append(t1+t2)
            after.append([t1,t2])
        if avail==[]:
            return -1
        max_index=comp.index(max(comp))
        max_juyuso=avail[max_index]
        juyusos.remove(max_juyuso)
        visit+=1
        return func(after[max_index][0],after[max_index][1],visit)
result=func(0,start_fuel,0)
print(result)


