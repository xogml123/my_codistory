n,k=map(int,input().split())
result=-1
frontier=[]
frontier.append(n)
visited=[]

while True:
    temp=[]
    result += 1
    for u in frontier:
        if u not in visited:
            visited.append(u)
        if u==k:
             break
        else:
            if u==0 and (u+1) not in visited :
                temp.append(u+1)
            else:
                if (u-1) not in visited:
                    temp.append(u-1)
                if (u+1) not in visited:
                    temp.append(u+1)
                if (2*u) not in visited:
                    temp.append(2*u)
    if u == k:
        break
    frontier=temp

print(result)


