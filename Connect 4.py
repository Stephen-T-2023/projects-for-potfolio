def draw (grid,row,collumn):
    print("")
    print("1 2 3 4 5")
    print("| | | | |")
    print(grid[0][0], grid[0][1], grid[0][2], grid[0][3], grid[0][4], )
    print(grid[1][0], grid[1][1], grid[1][2], grid[1][3], grid[1][4], )
    print(grid[2][0], grid[2][1], grid[2][2], grid[2][3], grid[2][4], )
    print(grid[3][0], grid[3][1], grid[3][2], grid[3][3], grid[3][4], "\n")

def add_piece(grid, collumn, player):

    if player == 1:
        piece = "B"
    else:
        piece = "R"

    collumn = collumn - 1

    i = 3
    check = 0

    while i > -1:
        if board[check][collumn] != "0":
            print("Invalid move, move will be forfeited")
            i = i - 5
        elif board[i][collumn] == "0":
            grid[i][collumn] = piece
            i = i - 5
        elif i > -1:
            i = i - 1
        else:
            print("Error")
    return grid

rows = int(input("Enter number of rows"))
collumns = int(input("Enter number of collumns"))
rows = rows - 1
collumns = collumns - 1
for i in range
board = [["0"*collumns]*rows]

won = False

draw(board, rows, collumns)

player = 1

while  won != True :
    
    print("It is player "  + str(player)  + "'s go.")
    c_choice = int(input("Enter the column number.  "))
    
    if c_choice<1 or c_choice>5:
        print("invalid move")
    else:
        board = add_piece(board, c_choice, player)

        draw (board, rows, collumns)

        if player == 1:
            player = 2
        elif player == 2:
            player = 1

print("Player "  + str(player) + " has won!")
input("Press enter to exit.")