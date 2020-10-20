ml,mr,tl,tr=input().split()

def rsp(a):
    if a[0]==a[1]:
        return 0
    elif (a[0]=='R') and (a[1]=='S') or (a[0]=='S') and (a[1]=='P') or (a[0]=='P') and (a[1]=='R'):
        return -1
    else:
        return 1
    
case=[]
result=[]
for i in [ml,mr]:
    for j in [tl,tr]:
        case.append([i,j])
for i in case:
    result.append(rsp(i))

if result[0]==-1 and result[1]==-1 or result[2]==-1 and result[3]==-1:
    print('MS')
elif result[0]==1 and result[2]==1 or result[1]==1 and result[3]==1:
    print('TK')
else:
    print('?')
        

        
        
