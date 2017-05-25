# Problem 1: 
# Use accumulative recursion to write the function duplicate_string
# that consumes a string s and a natural number n, and produces the
# new string containing n copies of s. Do not use the * operation.
# For example, duplicate_string("abc", 3) => "abcabcabc"
def make_copies(s,acc,n,count):
    if count==n:
        return acc
    else:
        
        return make_copies(s,acc+s,n,count+1)

def duplicate_string(s,n):
    return make_copies(s,s,n,1)
