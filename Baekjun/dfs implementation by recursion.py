


parent={}#nodes being visited

def dfs_one(graph,s):
    for node in adj[s]:
        if node not in parent:
            parent[node]=s
            #마킹이 필요하면 여기에
            dfs_one(graph,node)

def dfs(graph,vertexs):

    for node in vertexs:
        if node not in parent:
            parent[node]=None
            dfs_one(graph,node)
