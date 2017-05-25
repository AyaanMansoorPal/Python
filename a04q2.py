##
## *********************************
## Ayaan Mansoor Pal 
## *********************************
##



## check_upper_lower(v,u,l,n,i) consumes a list of values v, an upper
## value u, a lower value l, two counter n,i. n is a recursive counter
## i is the counter of how many times a value is replaced in v. The function
## mutates the list and returns counter i
## Effects: mutates v
## check_upper_lower: (listof Int) Int Int Int Int -> Int
## requires: l<=u
##           n=0 initially
##           i=0 initially
## Examples:
## for v=[1,2,3] 
## check_upper_lower(v,2,1,0,0)=> 1
## changes contents of L to [1,2,2]
## for v=[2,3]
## check_upper_lower(v,3,3,0,0)=> 2
## changes contents of L to [3,3]


def check_upper_lower(v,u,l,n,i):
    if n==len(v):
        return i
    else:
        if v[n]>u:
            v.remove(v[n])
            v.insert(n,u)
            i=i+1
            return check_upper_lower(v,u,l,n+1,i)
        elif v[n]<l:
            v.remove(v[n])
            v.insert(n,l)
            i=i+1
            return check_upper_lower(v,u,l,n+1,i)
        else:
            
            return check_upper_lower(v,u,l,n+1,i)




## put_in_bounds(values,lower,upper) consumes a number of values called values
## and two integers lower and upper. It produces the number of replacements that
## took place in values according to the conditions set according to upper and lower
## values is mutated according to the conditions
## Effects: mutates values
## put_in_bounds: (listof Int) Int Int -> Int
## requires: lower<=upper
## Examples and tests:
## See the function above as this function just returns the result
## of the function above



def put_in_bounds(values,lower,upper):
    initial_count=0
    initial_change_count=0
    return check_upper_lower(values,upper,lower,initial_count,initial_change_count)


    
    
