num,m=map(int,input().split())
num=list(map(int,list(str(num))))
purpose=len(num)-m
stack=[]
for x in num:
    #제거 할때
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)

for i in range(purpose):
    print(stack[i],end='')


