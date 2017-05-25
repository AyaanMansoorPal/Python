def dfs(graph, v):
    visited = []
    S = [v]
    while S != []:
        v = S.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                if w not in visited:
                    S.append(w)
    return visited


def bfs(graph,v):
    visited=[]
    Q=[]
    Q.append(v)
    while Q!=[]:
        v=Q.pop(0)
        visited.append(v)
        for n in graph[v]:
            if n not in visited and n not in Q:
                Q.append(n)
    return visited


def f25(L):
    d = {}
    for x in L:
        d[x] = L[x]
    for k in d:
        L[d[k]] = k

# What is the value of L after we run the following
L = [2,0,1]
f25(L)
