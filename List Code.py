##
## *********************************
## Ayaan Mansoor Pal 
## *********************************
##


## not_answered(student_answers) consumes a list of student answers, student_answers
## and produces the number of non-answered questions by the student
## not_answered: (listof Str)-> Int
## Examples:
## not_answered(["A","B","C"])=> 0
## not_answered(["A","","C"])=> 1
## not_answered(["","A","C"])=> 1

def not_answered(student_answers):
    if len(student_answers)==0:
        return 0
    else:
        return student_answers.count("")




## correct_answers(correct_ans,student_ans, count, n=0) consumes a list of correct answers,
## correct_ans, the student's answers, student_ans, and two counters, count and a default
## parameter n. Count,counts the number of correct answers by the student while n, recurses
## through the two lists comparing values.
## correct_answers: (listof Str) (listof Str) Int Int-> Int
## requires: n=0
##           count=0
##           both lists non-empty
##           both lists equal length
## Examples:
## correct_answers(["A","B","C"],["A","B","C"],0,0)=> 3
## correct_answers(["A"],["A"],0,0)=> 1
## correct_answers(["C"],["A"],0,0)=> 0
## correct_answers(["A","B","C"],["C","B","A"],0,0)=> 1
        
def correct_answers(correct_ans,student_ans,count,n=0):
    if n==len(student_ans):
        return count
    else:
        if student_ans[n]==correct_ans[n]:
            count=count+1
            return correct_answers(correct_ans[1:],student_ans[1:],\
                                   count,n)
        else:
            return correct_answers(correct_ans[1:],student_ans[1:],\
                                   count,n)



    
## incorrect_answers(correct,student_ans,i, n=0) consumes a list of the correct answers,correct
## and student answers, student_ans, and two counters, i and a default parameter n.
## It produces the number of incorrect answers by the student.
## incorrect_answers: (listof Str) (listof Str) Int Int -> Int
## requires: n=0
##           i=0
##           correct and student_ans are non-empty
##           correct and student_ans are the same length
## Examples:
## incorrect_answers(["A"],["B"],0,0)=> 1
## incorrect_answers(["A","B","C"],["A","B","C"],0,0)=> 0
## incorrect_answers(["A","B"],["C","D"],0,0)=> 2
        
        
def incorrect_answers(correct,student_ans,i,n=0):
    if n==len(student_ans):
        return i
    else:
        if (correct[n]!=student_ans[n]) and (student_ans[n]!=""):
            i=i+1
            return incorrect_answers(correct[1:],student_ans[1:],i,n)
        else:
            return incorrect_answers(correct[1:],student_ans[1:],i,n)



## clicker_results(solutions,student) consumes a solution and student and compares the two
## lists and produces the number of correct, the number answered and the number of questions
## unanswered by the student.[c,a,u]
## clicker_results: (listof Str) (listof Str) -> (listof Nat)
## requires: solutions and student are same length
## Examples:
## clicker_result([],[])=> [0,0,0]
## clicker_result(["A"],["A"])=>[1,1,0]
## clicker_result(["B"],[""])=> [0,0,1]

def clicker_results(solutions, student):
    if len(student)==0 and len(solutions)==0:
        return [0,0,0]
    else:    
        unanswered= not_answered(student)
        correct= correct_answers(solutions,student,0,)
        incorrect=incorrect_answers(solutions,student,0,)
        return [correct,(incorrect+correct),unanswered]




