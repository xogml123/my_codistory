n=int(input())

scores=[]
scores.extend(list(map(int,input().split())))
def round(num):

    if num-int(num)<0.5:
        return int(num)
    elif num-int(num)>=0.5:
        return int(num)+1

mean=sum(scores)/n

mean=round(mean)
scores.reverse()
max_score=0
min=1000000
min_index=0
for i in range(len(scores)):
    sub=scores[i]-mean
    if abs(sub)<min:
        min_index=len(scores)-i
        min=abs(sub)
        max_score=scores[i]
    elif abs(sub)==min and max_score<=scores[i]:
        min_index = len(scores) - i
        min = abs(sub)
        max_score = scores[i]

print(mean,min_index)








