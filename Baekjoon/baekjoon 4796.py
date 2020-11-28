import sys
rep=0
days=[]
while (1) :
    days.append(list(map(int,sys.stdin.readline().strip().split())))
    rep+=1
    if days[-1]==[0,0,0]:
        del days[-1]
        rep+=-1
        break
    
max_days=[]

for i in range(rep):
    
    q,r=divmod(days[i][2],days[i][1])
    if q==1 and r<days[i][0]:
        max_days.append(2*r+days[i][0]-r)
    elif q>=2 and r<days[i][0]:
        max_days.append(q*days[i][0]+r)
    elif q>=1 and r>=days[i][0]:
        max_days.append((q+1)*days[i][0])
        
    
for i in range(rep):
    print("Case {0}:".format(i+1),max_days[i])
    

