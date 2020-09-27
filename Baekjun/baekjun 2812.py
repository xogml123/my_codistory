n,k=map(int,input().split())

number=list(map(int,list(input())))
i=0
result=[]
while i<k:
    
    temp=number[:k-i+1]
    idx=temp.index(max(temp))
    i+=idx
    del number[:idx]
    result.append(number[0])
    del number[0]

print(''.join(list(map(str,result))))
        
    