k,n=map(int,input().split())
lines=[]
for i in range(k):
    lines.append(int(input()))
end=int(sum(lines)/n)
start=int(lines[0]/n)
cases=[i for i in range(end+1)]
def check_case(lines,case,n):
    sum=0
    for line in lines:
        sum+=line//case
    if sum>=n:
        return 1
    else:
        return 0
results=[]
def binary_search(cases,n,start,end):
    if end-start==1:
        target = cases[(end - start) // 2 + start]
        temp = check_case(lines, target, n)

        if temp == 1:
            results.append(target)
        return 0

    target=cases[(end-start)//2+start]
    temp=check_case(lines,target,n)
    if temp==1:
        results.append(target)
        start=(end-start)//2+start+1
        return binary_search(cases,n,start,end)
    else:
        end=(end-start)//2+start
        return binary_search(cases,n,start,end)
binary_search(cases,n,start,end)
print(max(results))


