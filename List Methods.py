##
## *********************************
## Ayaan Mansoor Pal 
## *********************************
##


## A Board is a (listof (listof (anyof 'X' 'O' ' ')) 
## requires: 
## * each list in a Board corresponds to a row of the
##   grid, and all lists are the same length,
## * Board is square,
## * Board contains at least one row.

## counter(board,i,total,char) consumes a list, board and a counter i,
## a character, char and total. Total stores the length of the filtered list
## which corresponds to the character, char. The function produces the length
## of the filtered list.
## counter: (listof (anyof'X','O',' ')) Int Int Str -> Int
## requires: total=0 initially
##           i=0 initially

## Examples:
## counter([['X','O'],[' ',' ']],0,0,'X')=> 1
## counter([['X','X'],['X','X']],0,0,'X')=> 4
## counter([' ',' ',' '],0,0,' ')=> 3

def counter(board,i,total,char):
    if i==len(board):
        return total
    else:
        total= len(list(filter (lambda x: x==char,board)))
        return counter(board,i+1,total,char)
    


## board_status(board,n,x,char) consumes a Board, board and two counters, n and
## x, where n is used to recurse and x stores the total of the times the character
## char appears on the board. The function produces the number of either, 'X','O',' '
## on the board, utilizing the counter function to move through the rows.
## board_status: Board Int Int Str -> Int
## requires: x=0
##           n=0
## Examples:
## board_status([["X","O"," ","X"],["X","O"," ","X"]],0,0,"X")=> 4
## board_status(["O","X"," "],0,0," ")=> 1
## board_status([["X"],["O"]],0,0,"O")=>1

def board_status(board,n,x,char):
    if n==len(board):
        return x
    else:
        x=counter(board[n],0,0,char)+board_status(board,n+1,x,char)
        
        return x

    
    

## game_status(b) consumes a Board b and produces the current game status according
## to the numbers of spaces or the number of pieces whether the game is in progress
## or the game is over or whether 'X' or 'O' won.
## game_status: Board -> Str
## Examples:
## game_status([[' ',' ',' ',' '], [' ',' ',' ',' '],
##             [' ',' ',' ',' '], [' ',' ',' ',' ']])=> "Game in progress"
## game_status([['X','O','X','X'], ['O','X','X','O'],
##             ['X','X','O','X'], ['X','X','X','O']])=> "Game over. X wins"
## game_status([['O','O','O','O'], ['O','O','X','O'],
##             ['X','X','O','X'], ['X','X','X','O']])=> "Game over. O wins"




def game_status(b):
    no_of_x=board_status(b,0,0,"X")
    no_of_o=board_status(b,0,0,"O")
    no_of_space=board_status(b,0,0," ")
    if no_of_space!=0:
        return "Game in progress"
    elif no_of_x==no_of_o and no_of_space==0:
        return "Game over. Tied"
    elif no_of_x> no_of_o and no_of_space==0:
        return "Game over. X wins"
    else:
        return "Game over. O wins"

##     
    
