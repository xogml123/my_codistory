import sys
x=input()

AB=[]
count=0
index=0

for ch in x:
    
    if ch=='X':
        count+=1
        if index==len(x)-1:
            if count%4==0:
                AB.append('A'*count)
            elif count%4==2:
                AB.append('A'*(count-2)+'BB')
            else:
                print(-1)
                sys.exit()
    elif ch=='.':
        if count%4==0:
            AB.append('A'*count)
        elif count%4==2:
            AB.append('A'*(count-2)+'BB')
        else:
            print(-1)
            sys.exit()
        AB.append('.')
        count=0
    index+=1

print(''.join(AB))
    
    
