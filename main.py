board = [
    [0,0,0,0,0,0,0,7,0],
    [5,0,3,0,1,0,9,0,2],
    [0,0,4,0,0,7,3,0,6],
    [7,2,0,0,4,0,6,0,9],
    [0,9,0,1,0,0,7,0,0],
    [6,0,0,2,0,0,0,0,0],
    [0,0,7,3,0,1,0,0,0],
    [0,0,0,0,0,0,0,5,0],
    [0,1,0,9,0,0,8,0,7]
]

def solve(board):
    find=find_empty(board)
    if not find:
        return True
    else:
        row,col=find
    
    for i in range(1,10):
        if valid(board,i,(row,col)):
            board[row][col]=i 

            if solve(board):
                return True
                
            board[row][col]=0

    return False


def valid(board,num,pos):

    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i]==num and i!=pos[1]:
            return False

    # check col
    for i in range(len(board)):
        if board[i][pos[1]]==num and i!=pos[0]:
            return False

    # check grid
    grid_x=pos[0]//3
    grid_y=pos[1]//3

    for i in range(3*grid_x,3*grid_x+3):
        for j in range(3*grid_y,3*grid_y+3):
            if board[i][j]==num and (i,j)!=pos:
                return False

    return True

def print_board(board):
    for i in range(len(board)):
        if i%3==0 :
            print("- - - - - - - - - - -")
        for j in range(len(board[i])):
            if j%3==0 and j!=0:
                print("| ",end='')
            if j==8:
                print(board[i][j])
            else:
                print(board[i][j],end=' ')
    print("- - - - - - - - - - -")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j)  # (row,column)
    return None

print_board(board)
solve(board)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
print_board(board)