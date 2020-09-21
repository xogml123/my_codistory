number=list(input())

str_num=['2','0','1','8']
a=[]
for i in range(4):
    a.append(number.count(str_num[i]))


if sum(a)!=len(number):
    print('0')
    
elif (a[0]==a[1]) and (a[2]==a[3]) and (a[1]==a[2]):
    print('8')
    
elif a[0]*a[1]*a[2]*a[3]!=0:
    print('2')
    
else:
    print('1')

    
    
    
    
    
