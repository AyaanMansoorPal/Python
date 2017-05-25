##
## *********************************
## Ayaan Mansoor Pal 
## *********************************
##

import check

## scores(team_names,vals) consumes a list of team_names and a list of items in
## the file and calculates the total scored by each team.
## scores: (listof Str) (listof (listof Str Int)) -> (listof (anyof Float Int))
## requires: len(team_names)>=1
##           len(vals) >=1

def scores(team_names,vals):
    score_sheet=[]
    total=0
    for i in team_names:
        total=0
        for j in vals:
            if i==j[0]:
                total=total+int(j[1])
        score_sheet.append(total)
    return score_sheet
    
## find_winner(filename) consumes a file and reads the team names and scores
## and adds up the score made by each team and produces the maximum score scored overall.
## Effects: contents of filename are read.
## find_winner: Str -> Int 
## requires: file to have specific fomrat
## Examples:
## If ex1.txt has one line, then
##   find_winner("ex1.txt") will produce the number scored by
##   the one team in the file
## If ex2.txt has line with 2 teams, then
##    find_winner("ex2.txt") will calculate the total score
##    and produce the max score achieved by either team.

def find_winner(filename):
    file_obj=open(filename,"r")
    line=" "
    team_names=[]
    val=[]
    while line != "":
          line=file_obj.readline()
          if line.split(",")[0] not in team_names and line.split(",")[0] !="":
              team_names.append(line.split(",")[0])
          if line.split(",")[0] !="":
              val=val+[line.split(",")]
    file_obj.close()      
    score=scores(team_names,val)
    max_val=max(score)
    return max_val

## Tests:
## Many teams with different score:
check.expect("Q1T1",find_winner("hogwarts.txt"),5)
## Two teams score same score:
check.expect("Q1T2",find_winner("ex1.txt"),7)
## Three different teams with different scores:
check.expect("Q1T3",find_winner("ex2.txt"),30)
## One team only in file:
check.expect("Q1T4",find_winner("ex3.txt"),10)
## One team with an array of scores:
check.expect("Q1T5",find_winner("ex4.txt"),10)


    
