n=int(input())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
def money1(d_element1):
    if d_element1==1:
        return 500
    elif d_element1>=2 and d_element1<4:
        return 300
    elif d_element1>=4 and d_element1<7:
        return 200
    elif d_element1>=7 and d_element1<11:
        return 50
    elif d_element1>=11 and d_element1<16:
        return 30
    elif d_element1>=16 and d_element1<22:
        return 10
    else:
        return 0
def money2(d_element2):
    if d_element2==1:
        return 512
    elif d_element2>=2 and d_element2<4:
        return 256
    elif d_element2>=4 and d_element2<8:
        return 128
    elif d_element2>=8 and d_element2<16:
        return 64
    elif d_element2>=16 and d_element2<32:
        return 32
    else: 
        return 0
def calc_money(d_element):
    return money1(d_element[0])+money2(d_element[1])
for i in range(n):
    print(calc_money(data[i])*10000)
