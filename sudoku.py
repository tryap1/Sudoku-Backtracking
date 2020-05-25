#Define a SOLVABLE sudoku board
board = [
    [0,0,0,0,0,0,0,0,0],
    [0,1,5,3,0,9,7,8,0],
    [0,4,0,2,0,1,0,6,0],
    [0,6,4,7,0,8,1,2,0],
    [0,0,0,0,0,0,0,0,0],
    [0,3,7,5,0,6,8,4,0],
    [0,8,0,4,0,5,0,9,0],
    [0,7,9,8,0,2,4,3,0],
    [0,0,0,0,0,0,0,0,0]
]
#Sudoku solving function
def sudoku_solve(board):
    #reached the end when you can no longer find blanks

    if not find_blanks(board):
        return True
    else:
        blank = find_blanks(board)
    for i in range(1,10):

        #insert potential answer into blank and check if answer is possible
        if check_valid(board,i,blank) == True:
            #if true insert answer into board
            board[blank[0]][blank[1]] = i

            #recursively call function to check answer in board
            if sudoku_solve(board) == True:
                return True
            #if cannot solve: wrong answer, go back and reset last blank
            else:
                board[blank[0]][blank[1]] = 0 #reset the last blank ie backtrack

    return False



#function to check validity of input, test is an insertable integer to test, blank is a tupple of pos
def check_valid(board,test,blank):
    #check column
    for i in range(len(board[0])):
        if board[i][blank[1]] == test and blank[0] != i:
            return False
    #check column
    for j in range(len(board)):
        if board[blank[0]][j] == test and blank[1] != j:
            return False
    #check quardrant
    quad_col = blank[1]//3
    quad_row = blank[0]//3

    for i in range(quad_row*3, quad_row*3+3):
        for j  in range(quad_col*3, quad_col*3+3):
            if board[i][j] == test and (i,j) != blank:
                return False

    return True

#this function takes in a board and returns coordinates of first available blank
def find_blanks(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None




def print_board(board):
    for i in range(len(board)):
        if i % 3 ==0 and i !=0:
            print("____________________")
        for j in range(len(board[0])):
            if j % 3 ==0 and j !=0:
                print("|", end = '')
            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j])+' ', end='')


print_board(board)
print("__________________________")
sudoku_solve(board)
print_board(board)