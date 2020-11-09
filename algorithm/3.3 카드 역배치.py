cards=[i for i in range(1,21)]
sections=[]
def partReverse(section,cards):
    if section[1]!=19:
        a1=cards[:section[0]]
        temp=cards[section[0]:(section[1]+1)]
        temp.reverse()
        a2=temp
        a3=cards[section[1]+1:]
        a1.extend(a2)
        a1.extend(a3)
        return a1
    elif section[1]==19:
        a1 = cards[:section[0]]
        temp = cards[section[0]:(section[1] + 1)]
        temp.reverse()
        a2 = temp
        a1.extend(a2)
        return a1

for i in range(10):
    temp=(list(map(int,input().split())))
    temp[0]-=1
    temp[1]-=1
    sections.append(temp)
for section in sections:
    cards=partReverse(section,cards)

for card in cards:
    print(card,end=' ')

