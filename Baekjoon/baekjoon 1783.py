n,m=map(int,input().split())
num=1
if n==1:
    num=1
elif n==2:
    if m<3:
        num=1
    elif m>=3 and m<5:
        num=2
    elif m>=5 and m<7:
        num=3
    elif m>=7 and m<9:
        num=4
    else:
        num=4

elif n>=3:
    if m<5:
        num=m
    elif m==6 or m==5:
        num=4
    elif m>=7:
        num=m-2

print(num)
    

