##
## *********************************
## Ayaan Mansoor Pal (20655883)
## CS 116 Winter 2017
## Assignment 09, Problem 3
## *********************************
##

import check

## Useful constants and examples:
A = {"Dan": [" Carlos "], " Carlos ": ["Dan"], "Bob": ["Ali", "Eve"],
" Feng ": ["Pat", "Ted", " Heidi "], "Ted": [" Feng "],
" Heidi ": [" Feng ", "Sai"], "Ali": ["Bob", "Eve"], " Maria ": [],
"Eve": ["Bob", "Ali"], "Pat": [" Feng "], "Sai": [" Heidi "]}

B={"Harry":[]}

C={"Harry":[],"Bob":[],"Mike":[]}

D={"Harry":["Zoe","Murtle","Conrad"],"Zoe":[],"Murtle":[],"Conrad":[]}

E={"Megan":[0,2],"Polly":[3.3,4],2:["Megan"],0:["Megan"],3.3:["Polly"],4:["Polly"]}
F={2:[0.2],0.2:[2]}
G={}
H={"Carrie":["John","Simon"],"John":["Carrie"],"Simon":["Carrie"],"James":["Mike","Jonas"],
   "Mike":["James"],"Jonas":["James"],"Justin":[]}

# bfs(graph, v): breadth-first search on graph starting at v.
## As described in notes used for traversal in a graph
## bfs: (dictof (anyof Str Int Float) (anyof Str Int Float))-> (listof (anyof Str Int Float))

def bfs(graph,v):
    visited=[]
    Q=[]
    Q.append(v)
    while Q!=[]:
        v=Q.pop(0)
        visited.append(v)
        for n in graph[v]:
            if n not in Q and n not in visited:
                Q.append(n)
    return visited
                
       
## find_largest(graph) consumes an adjaceny list,graph and produces the number
## of vertices in the largest connected component of the graph.
## find_largest: (dictof (anyof Str Int Float)) -> Int
## Examples:
## find_largest(A) => 5
## find_largest(B) => 1

def find_largest(graph):
  if graph=={}:
        return 0
  else:
    Q=[]
    passed=[]
    a_list=[]
    length=[]
    for n in graph:
        Q.append(n)
    for i in Q:
        if i not in passed:
            v=i
            a_list.append(bfs(graph,v))
            list_so_far=bfs(graph,v)
            for j in list_so_far:
                passed.append(j)
    for k in a_list:
        length.append(len(k))
    return max(length)

## Tests:
check.expect("Q3T1",find_largest(A),5)
check.expect("Q3T2",find_largest(B),1)
check.expect("Q3T3",find_largest(C),1)
check.expect("Q3T4",find_largest(D),4)
check.expect("Q3T5",find_largest(E),3)
check.expect("Q3T6",find_largest(G),0)
check.expect("Q3T7",find_largest(F),2)
check.expect("Q3T8",find_largest(H),3)


            
    
