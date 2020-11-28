import math
n=int(input())
def isPrime(x):
    if x==1:
        return None
    if x==2:
        return 2
    else:
        indicator=0
        for i in range(2,int(math.sqrt(x)+2)):
            if x%i==0:
                indicator=1
                break
        if indicator==0:
            return x

def reverse(x):
    temp=list(str(x))
    temp.reverse()
    return int(''.join(temp))

nums=list(map(int,input().split()))

for num in nums:
    rnum=reverse(num)
    ip=isPrime(rnum)
    if ip!=None:
        print(isPrime(rnum),end=' ')
