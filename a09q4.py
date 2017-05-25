##
## *********************************
## Ayaan Mansoor Pal (20655883)
## CS 116 Winter 2017
## Assignment 09, Problem 4
## *********************************
##

import check

## A Tree is a (list Nat (listof Tree))
## requires:
## * the first item is a Nat representing the label of the vertex
## * the second item is a list of vertices directly below
## * is a list of length two

## Useful examples and constants for a Tree:
A=[3,[[4,[]],[1,[]],[2,[]],[0,[]]]]
B=[0,[[1,[[4,[]],[5,[]]]],[2,[[6,[]],[7,[]]]],[3,[[8,[]],[9,[]]]]]]
C=[0,[[1,[[4,[]],[2,[]],[3,[]]]]]]
D=[0,[[1,[[3,[[2,[]]]]]]]]
E=[1,[[0,[]],[2,[]]]]
F=[0,[[1,[[2,[]],[3,[]]]],[]]]
G=[1,[[0,[[2,[]],[3,[]]]],[4,[]]]]
H=[4,[[1,[[0,[]],[3,[]]]],[2,[[5,[]],[]]]]]
I=[0,[[4,[[5,[]],[3,[]]]],[2,[[1,[]],[6,[]]]]]]
U = [0 ,[[1 , []] ,[2 , []]]]
V = [3 , [[1 , []] ,[0 , [[2 , []] ,[5 , []]]] ,[4 , []]]]
T=[0,[]]

## make_matrix(n) consumes a natural number n and produces an initialized matrix
## with all values as 0.
## make_matrix: Nat -> (listof (listof 0))

def make_matrix(n):
    int_list=[]
    matrix=[]
    for i in range(n):
       int_list=[]
       for j in range(n):
          int_list.append(0)
       matrix.append(int_list)
    return matrix

## process_child(tree,matrix,parent) consumes the matrix,a tree and a parent node
## and processes the child nodes and updates the matrix accordingly recursively.
## Effects: mutates the matrix accordingly and produces None.
## process_child: Tree (listof (listof (anyof 0 1))) Nat -> None

def process_child(tree,matrix,parent):
    for i in tree:
     if i!=[]:
        if type(i[0])==int:
            child=i[0]
            matrix[parent][child]=1
            matrix[child][parent]=1
        if type(i[1])==list and i[1]!=[]:
           return process_child(i[1],matrix,i[0])

## process_tree(tree,matrix,parent) consumes the matrix,a tree and a parent node
## and processes the child nodes according to the parent node and updates the matrix
## accordingly and produces None.
## Effects: mutates the matrix accordingly
## process_tree: Tree (listof (listof (anyof 0 1))) Nat -> None
        
def process_tree(tree,matrix,parent):
    for i in tree:
       if i!=[]:
         if type(i[0])==int:
           child=i[0]
           matrix[parent][child]=1
           matrix[child][parent]=1
         if type(i[0])==int and i[1]!=[]:
           process_child(i[1],matrix,i[0])

## tree_to_matrix(tree,size) consumes a tree and the size of the Tree and produces
## an adjacency matrix which describes the same graph as tree.
## tree_to_matrix: Tree Nat -> (listof (listof (anyof 0 1)))
## Examples:
## tree_to_matrix(T,1) => [[0]]
## tree_to_matrix(U,3) => [[0,1,1],[1,0,0],[1,0,0]]
## tree_to_matrix(E,3) => [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
           
def tree_to_matrix(tree,size):
    matrix=make_matrix(size)
    parent=tree[0]
    process_tree(tree[1],matrix,parent)
    return matrix
    
## Tests:
check.expect("Q4T1",tree_to_matrix(T,1),[[0]])
check.expect("Q4T2",tree_to_matrix(U,3),[[0,1,1],[1,0,0],[1,0,0]])
check.expect("Q4T3",tree_to_matrix(V,6),[[0,0,1,1,0,1],[0,0,0,1,0,0],[1,0,0,0,0,0],
                                         [1,1,0,0,1,0],[0,0,0,1,0,0],[1,0,0,0,0,0]])
check.expect("Q4T4",tree_to_matrix(A,5),[[0,0,0,1,0],[0,0,0,1,0],[0,0,0,1,0],
                                         [1,1,1,0,1],[0,0,0,1,0]])
check.expect("Q4T5",tree_to_matrix(B,10),[[0,1,1,1,0,0,0,0,0,0],[1,0,0,0,1,1,0,0,0,0],
                                          [1,0,0,0,0,0,1,1,0,0],[1,0,0,0,0,0,0,0,1,1],
                                          [0,1,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],
                                          [0,0,1,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],
                                          [0,0,0,1,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0]])
check.expect("Q4T6",tree_to_matrix(C,5),[[0,1,0,0,0],[1,0,1,1,1],[0,1,0,0,0],[0,1,0,0,0],
                                         [0,1,0,0,0]])
check.expect("Q4T7",tree_to_matrix(D,4),[[0,1,0,0],[1,0,0,1],[0,0,0,1],[0,1,1,0]])
check.expect("Q4T8",tree_to_matrix(E,3),[[0, 1, 0], [1, 0, 1], [0, 1, 0]])
check.expect("Q4T9",tree_to_matrix(F,4),[[0,1,0,0],[1,0,1,1],[0,1,0,0],[0,1,0,0]])
check.expect("Q4T10",tree_to_matrix(G,5),[[0,1,1,1,0],[1,0,0,0,1],[1,0,0,0,0],[1,0,0,0,0],
                                          [0,1,0,0,0]])
check.expect("Q4T11",tree_to_matrix(H,6),[[0, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 1],
                                          [0, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]])
check.expect("Q4T12",tree_to_matrix(I,7),[[0,0,1,0,1,0,0],[0,0,1,0,0,0,0],[1,1,0,0,0,0,1],[0,0,0,0,1,0,0],
                                          [1,0,0,1,0,1,0],[0,0,0,0,1,0,0],[0,0,1,0,0,0,0]])
    
