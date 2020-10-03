
adj={}  #directory which indicates adjacency




def bfs(graph,s):
    level={s:0}
    new_visit={s}
    parent={s:None}
    i=1          #level indicator
    while new_visit:
        next=[]
        for u in new_visit:
            for node in adj[u]:
                if node not in level:
                    level[node]=i
                    parent[node]=u
                    next.append(node)
        new_visit=next
        i+=1
                
                
            
       
        
