import sys

inp=sys.stdin.readlines()
i=0
result=[]
while '-' not in inp[i]:
    num=0
    stk=[]
    for bracket in inp[i]:
        if bracket=='{':
            stk.append(bracket)
        elif bracket=='}' and len(stk)==0:
            stk.append('{')
            num+=1
        elif bracket=='}' and len(stk)!=0:
            temp=stk[len(stk)-1]
            if temp=='{':
                stk.pop()
            elif temp=='}':
                stk.extend(['}'])
    num +=int(len(stk) / 2)
    result.append(num)

    i+=1
for i in range(1,len(result)+1):
    print('{0}. {1}'.format(i,result[i-1]))









