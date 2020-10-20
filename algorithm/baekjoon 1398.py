import sys
from math import log10
inp=sys.stdin.readlines()

n=int(inp[0].strip('\n'))

for i in range(n):
    test=int(inp[i+1].strip('\n'))
    num=0
    while test:
        k=log10(test)
        integer=int(k)

        if integer%2==0:
            coin=10**integer
        if integer%2==1 and test/10**integer<2.5:
            coin=10**integer
        if integer%2==1 and test/10**integer>=2.5:
            coin=2.5*10**integer
        coin=int(coin)
        q,r=divmod(test,coin)
        test=int(r)
        num+=int(q)
    print(num)


