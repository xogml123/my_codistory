n=int(input())

sinkers=list(map(int,input().split()))
sinkers.sort(reverse=True)

def greedy(weight):
    
    for sinker in sinkers:
        weight-=sinker
        if weight<0:
            weight+=sinker
            continue
        elif weight==0:
            return 1
    return 0
        
    

w=0

while(1):
    w+=1
    sign=greedy(w)
    if sign==0:
        break
    elif sign==1: 
        continue
    
  
print(w)

    
