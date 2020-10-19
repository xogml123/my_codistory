n=int(input())
num=0

for i in range(1,n+1):
    temp=list(map(int,list('{0}'.format(i))))
    if len(temp)==1:
        num+=1
    else:
        diff=temp[1]-temp[0]
        str=0
        for j in range(len(temp)-1):
            if diff!=temp[j+1]-temp[j]:
                str+=1
        if str==0:
            num+=1

print(num)
        
    
