# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:04:52 2020

@author: Administrator
"""
n,m,v=map(int,input().split())

edges=[]
graph={}
graph_bfs={}
graph_dfs={}

for i in range(m):
    edges.append(list(map(int,input().split())))

for edge in edges:
    temp=[]
    temp.append(edge[1])
    temp.append(edge[0])
    
for i in range(1,n+1):
    graph[i]=[]

for i in range(1,n+1):
    for edge in edges:
        if edge[0]==i:
            graph[i].append(edge[1])
        elif edge[1]==i:
            graph[i].append(edge[0])
        else:
            continue

for key in graph:
    graph_bfs[key]=sorted(graph[key])
    
for key in graph_bfs:
    graph_dfs[key]=sorted(graph_bfs[key],reverse=True)
    
        
def bfs(graph,v):
    visit=[]
    need_visit=[]
    need_visit.append(v)
    
    while need_visit:
        node=need_visit.pop(0)
        if node not in visit:
            
            visit.append(node)
            need_visit.extend(graph[node])
    return visit

def dfs(graph,v):
    visit=[]
    need_visit=[]
    need_visit.append(v)
    
    while need_visit:
        node=need_visit.pop()
        if node not in visit:
            
            visit.append(node)
            need_visit.extend(graph[node])
    return visit

print(' '.join(list(map(str,dfs(graph_dfs,v)))))
print(' '.join(list(map(str,bfs(graph_bfs,v)))))



    
