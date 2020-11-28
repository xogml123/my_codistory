string=list(input())
nums='0123456789'
number=[]
def divisor(x):
    temp=[]
    for i in range(1,x+1):
        if x%i==0:
            temp.append(i)
    return temp

for ch in string:
    if ch in nums:
        number.append(ch)
    else:
        continue
result=int(''.join(number))
divisors=divisor(result)
print(result)
print(len(divisors))