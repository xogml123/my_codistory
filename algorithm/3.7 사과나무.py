n=int(input())
trees=[]
result=0
for i in range(n):
    trees.append(list(map(int,input().split())))
edges=[]
for i in range(n):
    for j in range(n//2-i):
        edges.append(trees[i][j])
for i in range(n):
    for j in range(n//2+1+i,n):
        edges.append(trees[i][j])
for i in range(n):
    for j in range(n//2-(n-1-i)):
        edges.append(trees[i][j])
for i in range(n):
    for j in range(n//2+1+(n-1-i),n):
        edges.append(trees[i][j])
for i in range(n):
    result+=sum(trees[i])
result-=sum(edges)
print(result)

