t=int(input())
a=300
b=60
c=10
buttons=[a,b,c]
result=[]
for i in range(len(buttons)):
    q,r=divmod(t,buttons[i])
    result.append(q)
    t=r
if t!=0:
    print(-1)
else:
    result=list(map(str,result))
    print(' '.join(result))
