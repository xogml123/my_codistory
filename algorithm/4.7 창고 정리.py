l=int(input())
heights=list(map(int,input().split()))
m=int(input())

for i in range(m):
    max_i=heights.index(max(heights))
    min_i=heights.index(min(heights))
    heights[max_i]-=1
    heights[min_i]+=1

print(max(heights)-min(heights))