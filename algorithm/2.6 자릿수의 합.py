n=int(input())
nums=list(map(int,input().split()))
sums=[]

def digit_sums(x):
    return sum(list(map(int,list(str(x)))))

for num in nums:
    sums.append(digit_sums(num))
print(nums[sums.index(max(sums))])