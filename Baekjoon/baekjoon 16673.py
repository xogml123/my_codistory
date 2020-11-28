n,k,p=map(int,input().split())
wine=0
for c in range(0,n+1):
    wine+=k*c+p*c**2
    
print(wine)
    
