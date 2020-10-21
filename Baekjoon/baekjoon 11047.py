n,k=list(map(int,input().split()))
coin=[]
for i in range(n):
    coin.append(int(input()))
               
                
coin.reverse()
num=0
for c in coin:
    if c>k:
        continue
    else:
        q,r=divmod(k,c)
        num+=q
        k=r
print(num)

                
    
