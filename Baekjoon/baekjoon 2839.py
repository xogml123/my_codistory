N=int(input())

a,b=divmod(N,5)

if b==0:
    print(a)
else:
    for i in range(a,-1,-1):
        c,d=divmod(N-5*i,3)
        if d==0:
            print(i+c)
            break
    if i==0 and d!=0:
        print(-1)
         
    
        
    
    
    
