n=int(input())
corrections=list(map(int,input().split()))
scores=[]
for cor in corrections:
    if cor==0:
        scores.append(0)
    elif cor==1 and scores!=[]:
        temp=scores[len(scores)-1]
        scores.append(temp+1)
    elif cor==1 and scores==[]:
        scores.append(1)
print(sum(scores))
