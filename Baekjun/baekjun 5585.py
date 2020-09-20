import sys


price=int(sys.stdin.readline())
remain=1000-price
coins=[500,100,50,10,5,1]
temp=remain
sum=0
for coin in coins:
    q,r=divmod(temp,coin)
    sum+=q
    temp=r
    
print(sum)
    
