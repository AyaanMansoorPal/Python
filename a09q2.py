##
## *********************************
## Ayaan Mansoor Pal 
## *********************************
##

import check

## check_first(first,length) the first line in the file and the length of the
## first line written into the file and produces the next line according to the given conditions.
## check_first: Str Nat -> (listof (anyof "." "X"))
## requires: len(first) >= 1

def check_first(first,length):
    list_of_next=[]
    for i in range(length):
        if i==0:
           list_of_next.append(".")
        elif i+1==len(first):
           list_of_next.append(".")
        elif first[i]=="X" and first[i+1]!="X" and first[i-1]!="X":
           list_of_next.append("X")
        elif first[i]!="X" and first[i+1]=="X" and first[i-1]!="X":
           list_of_next.append("X")
        elif first[i]!="X" and first[i+1]!="X" and first[i-1]=="X":
           list_of_next.append("X")
        else:
           list_of_next.append(".")
    return list_of_next

## automaton(filename,padding,nlines) consumes a file, filename and the number of lines to be written
## onto the file,nlines and the "padding" which is needed to construct a line and produces None
## Effects: writes a constructed line according to the conditions onto the file on a new line.
## automaton: Str Nat Nat -> None
## Examples:
## If automaton("ex1.txt",1,1), then
## ".X." is written onto the file
## If automaton("ex2.txt",2,1),then
## "..X.." is written onto the file

def automaton(filename,padding,nlines):
    file_obj=open(filename,"w")
    dot="."*padding
    first=dot+"X"+dot+"\n"
    length=len(first)-1
    file_obj.write(first)    
    for i in range(nlines-1):
        first=check_first(first,length)
        line="".join(first)
        line=line[:len(line)-1]+(line[len(line)-1]+"\n")
        file_obj.write(line)
    file_obj.close()
    return None

## Tests:
## Test 1:
check.set_file_exact("Test.txt","ex1_expected.txt")
check.expect("Q2T1",automaton("Test.txt",1,1),None)
## Test 2:
check.set_file_exact("Test.txt","ex2_expected.txt")
check.expect("Q2T2",automaton("Test.txt",2,1),None)
## Test 3:
check.set_file_exact("Test.txt","ex3_expected.txt")
check.expect("Q2T3",automaton("Test.txt",2,2),None)
## Test 4:
check.set_file_exact("Test.txt","a-4-4.txt")
check.expect("Q2T4",automaton("Test.txt",4,4),None)
## Test 5:
check.set_file_exact("Test.txt","a-3-5.txt")
check.expect("Q2T5",automaton("Test.txt",3,5),None)
## Test 6:
check.set_file_exact("Test.txt","a-8-3.txt")
check.expect("Q2T6",automaton("Test.txt",8,3),None)
## Test 7:
check.set_file_exact("Test.txt","ex4_expected.txt")
check.expect("Q2T7",automaton("Test.txt",3,3),None)
## Test 8:
check.set_file_exact("Test.txt","ex1.txt")
check.expect("Q2T8",automaton("Test.txt",1,0),None)
## Test 9:
check.set_file_exact("Test.txt","ex2.txt")
check.expect("Q2T9",automaton("Test.txt",10,2),None)


