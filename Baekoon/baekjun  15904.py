words=input()
i=0
target='UCPC#'
for ch in words:
    if ch==target[i]:
        i+=1
    else:
        continue
if i==4:
    print('I love UCPC')
else:
    print('I hate UCPC')
    

