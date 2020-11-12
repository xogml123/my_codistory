parens=list(input())
stack=[]
before=None
result=0
for paren in parens:
    #stack 비었을때
    if len(stack) ==0:
        stack.append(paren)

    #쇠막대 있는 상태
    elif len(stack) >=1:
        if paren =='(':
            stack.append(paren)
         #레이저 쇠막대 절단
        elif paren == ')' and before=='(':
            result+=len(stack)-1
            stack.pop()
        elif paren==')' and before==')':
            result+=1
            stack.pop()
    before=paren
print(result)


