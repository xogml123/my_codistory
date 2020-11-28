
num,m=map(int,input().split())
num=list(map(int,list(str(num))))
m_origin=m
result=[]
complement=0
while True:
    if m==0:

        result.extend(num[complement:])
        break
    elif m!=0 and len(result)==len(num)-m_origin:
        break
    else:
        temp=num[complement:complement+m+1]
        max_index=temp.index(max(temp))
        result.append(temp[max_index])
        m-=max_index
        complement+=max_index+1

print(int(''.join(list(map(str,result)))))









