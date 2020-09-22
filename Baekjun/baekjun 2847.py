n=int(input())
scores=[0]
for i in range(n):
    scores.append(int(input()))
num=0
for i in range(n-1,0,-1):
    if scores[i]>=scores[i+1]:
        num+=scores[i]-scores[i+1]+1
        scores[i]=scores[i+1]-1
   
print(num)

        
        