def initialize(length):
    row=[]
    matrix=[]
    for j in range(length):
      row=[]
      for i in range(length):
        row.append(0)
      matrix.append(row)
    return matrix
        


def make_ad(edge,matrix):
    for j in edge:
       matrix[j[0]][j[1]]=1
       matrix[j[1]][j[0]]=1
    


def edge_to_matrix(edge):
    val=[]
    for i in edge:
        if i[0] not in val:
            val.append(i[0])
        if i[1] not in val:
            val.append(i[1])
    val.sort()
    matrix=initialize(len(val))
    make_ad(edge,matrix)
    return matrix
    
    
