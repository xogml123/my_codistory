import sys

inp=sys.stdin.readlines()
n,w=map(int,inp[0].split())

prices=[]
for i in range(0,n+1):
    if i==0:
        prices.append(1000000000000000000)
    else:
        prices.append(int(inp[i].strip('\n')))
prices.append(0)

def max_money(prices,n,w):
    coin=0
    flip=0
    for i in range(1,n+1):
        if prices[i]<prices[i-1] and prices[i]<= prices[i+1] and flip==0:
            q,r=divmod(w,prices[i])
            coin+=q
            w-=q*prices[i]
            flip+=1
        if prices[i]>prices[i-1] and prices[i]>= prices[i+1] and flip==1:
            w+=coin*prices[i]
            coin=0
            flip=0
    return w
print(max_money(prices,n,w))







