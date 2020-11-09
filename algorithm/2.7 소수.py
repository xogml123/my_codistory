import math
n=int(input())
primes=[2]

for i in range(3,n+1):
    indicator=0
    for j in range(2,int(math.sqrt(i)+2)):
        if i%j==0:
            indicator=1
            break
    if indicator==0:
        primes.append(i)

print(len(primes))


