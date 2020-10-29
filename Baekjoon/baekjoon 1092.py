import sys
inp=sys.stdin.readlines()

n=int(inp[0].strip('\n'))

crains=list(map(int,inp[1].split()))

m=int(inp[2].strip('\n'))

boxes=list(map(int,inp[3].split()))

crains.sort(reverse=True)
boxes.sort(reverse=True)

if crains[0]<boxes[len(boxes)-1]:
    print(-1)
else:
    num=0

    while boxes!=[0]*len(boxes):
        j = 0
        while j<len(crains):
            for i in range(len(boxes)):
               if boxes[i]==0:
                   pass
               else:
                   if boxes[i]<=crains[j]:
                       boxes[i]=0
                       j+=1
                   else:
                       continue


        num+=1
    print(num)



