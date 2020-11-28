n=int(input())

words=[]
for i in range(n):
    words.append(list(input().lower()))
i=0
for word in words:
    i+=1
    temp=word.copy()
    word.reverse()
    if temp==word:
        print('#{0} YES'.format(i))
    else:
        print('#{0} NO'.format(i))


