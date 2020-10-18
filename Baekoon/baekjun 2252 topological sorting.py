import sys

inp=sys.stdin.readlines()

n,m=inp[0].split()
comparisons=[]
adj={}
for i in range(1,m):
    comparisons.append(inp[i].split())

for comp in comparisons:
    if comp[0] not in adj:
        adj[comp[0]]=0
    
    adj[comp[0]]

for comp in comparisons:
    if comp[1] not in




