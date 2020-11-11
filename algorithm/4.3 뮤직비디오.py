n,m=map(int,input().split())

songs=list(map(int,input().split()))
start=sum(songs)//m
end=(n//m+1)*max(songs)+1

dvds=[i for i in range(end+1)]
results=[]
def dvd_check(dvd):
    temp = 0
    dvd_num = 0
    for song in songs:
        temp += song
        if temp > dvd:
            dvd_num += 1
            temp = song
        elif temp == dvd:
            dvd_num+=1
            temp=0
    if temp!=0:
        dvd_num+=1
    return dvd_num
def binary_search(m,start,end):
    target=(end-start)//2+start
    dvd=dvds[target]
    dvd_num=dvd_check(dvd)
    if end-start==0:
        return 0
    else:
        if dvd_num==m:
            results.append(dvd)
            end=target
            return binary_search(m,start,end)
        elif dvd_num > m:
            start=target+1
            return binary_search(m,start,end)
        elif dvd_num< m:
            results.append(dvd)
            end=target
            return binary_search(m,start,end)
binary_search(m,start,end)
print(min(results))

