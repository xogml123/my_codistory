n,m=map(int,input().split())

nums=list(map(int,input().split()))
nums.sort()

def binary_search(m,start,end):
    target=(end-start)//2+start
    if m==nums[target]:
        return target
    elif m<nums[target]:
        end=target
        return binary_search(m,start,end)
    elif m>nums[target]:
        start=target+1
        return binary_search(m,start,end)

print(binary_search(m,0,len(nums))+1)



