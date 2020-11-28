n=int(input())

seats=list(input())
cup=2
i=0
avail=0
for seat in seats:
    if seat=='S':
        avail+=1
        i+=1
    if seat=='L':
        avail+=1
        del seats[i]
        i+=1
print(avail+1)
    
        