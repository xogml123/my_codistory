t=int(input())

for i in range(t):
    nums=[]
    n,s,e,k=map(int,input().split())
    nums=list(map(int,input().split()))
    srtnums=sorted(nums[s-1:e])
    print("#{0} {1}".format((i+1),srtnums[k-1]))
