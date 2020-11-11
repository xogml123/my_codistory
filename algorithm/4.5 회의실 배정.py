n=int(input())
times=[]
for i in range(n):
    times.append(list(map(int,input().split())))

times.sort(key=lambda x:x[1])
end=1
result=0
for i in range(n):
    if times[i][0]>=end:
        result+=1
        end=times[i][1]

print(result)
