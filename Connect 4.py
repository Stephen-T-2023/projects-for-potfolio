def check_horizontal_win(grid, player):
    for row in grid:
        for col in range(len(row) - 3):
            if player == 1:
                if all(cell == "B" for cell in row[col:col + 4]):
                    return True
            else:
                if all(cell == "R" for cell in row[col:col + 4]):
                    return True
    return False

def check_vertical_win(grid, player):
    for col in range(len(grid[0])):
        for row in range(len(grid) - 3):
            if player == 1:
                if all(grid[row + i][col] == "B" for i in range(4)):
                    return True
            else:
                if all(grid[row + i][col] == "R" for i in range(4)):
                    return True
    return False

def check_diagonal_win(grid, player):
    for row in range(len(grid) - 3):
        for col in range(len(grid[0]) - 3):
            if player == 1:
                if all(grid[row + i][col + i] == "B" for i in range(4)):
                    return True
            else:
                if all(grid[row + i][col + i] == "R" for i in range(4)):
                    return True

            if player == 1:
                if all(grid[row + i][col + 3 - i] == "B" for i in range(4)):
                    return True
            else:
                if all(grid[row + i][col + 3 - i] == "R" for i in range(4)):
                    return True
                
    return False

def draw(grid, rows, cols):
    for row in range(rows):
        for col in range(cols):
            print(grid[row][col], end=' ')
        print()

def add_piece(grid, column, player, row):
    if player == 1:
        piece = "B"
    else:
        piece = "R"

    column = int(column)

    while row >= 0:
        if grid[row][column] != "0":
            row -= 1
        else:
            grid[row][column] = piece
            break
    else:
        print("Invalid move, move will be forfeited")

end = "N"

player_1_wins = 0
player_2_wins = 0

while end == "N":

    input1 = False
    input2 = False

    rows = input("Enter the number of rows (Must be at least 4): ")

    while input1 == False:
        try:
            rows = int(rows)
            if rows < 4:
                rows = input("Please enter a number that is at least equal to 4: ")
            else:
                input1 = True

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            rows = input("Please enter a whole number greater than 4: ")
            
    cols = input("Enter the number of columns (Must be at least 4): ")

    while input2 == False:
        try:
            cols = int(cols)
            if cols < 4:
                cols = input("Please enter a number that is at least equal to 4: ")
            else:
                input2 = True

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            cols = input("Please enter a whole number greater than 4: ")

    grid = [["0" for _ in range(cols)] for _ in range(rows)]

    draw(grid, rows, cols)
    won = False
    player = 1

    while won != True:
        print("It is player " + str(player) + "'s go.")

        input3 = False

        c_choice = input("Enter the column number: ")

        while input3 == False:
            try:
                c_choice = int(c_choice)
                if c_choice > cols or c_choice < 1:
                    c_choice = input("Please enter a number that is less than", cols, "and larger than 0: ")
                else:
                    input3 = True

            except Exception as e:
                print(f"An error occurred: {str(e)}")
                c_choice = input("Please enter a whole number: ")

        if c_choice < 1 or c_choice > cols:
            print("Invalid move")
        else:
            add_piece(grid, c_choice - 1, player, rows - 1)
            draw(grid, rows, cols)

        if check_horizontal_win(grid, player) or check_vertical_win(grid, player) or check_diagonal_win(grid, player):
            won = True

        if not won:
            if player == 1:
                player = 2
            else:
                player = 1

    print("Player " + str(player) + " has won!")
    if player == 1:
        player_1_wins += 1
    else:
        player_2_wins += 1

    print("Player 1 has", player_1_wins, "wins, Player 2 has", player_2_wins, "wins.")

    end = input("Would you like to quit? Y or N: ").upper()
    
    while end != "Y" and end != "N":
            end = input("Y or N: ").upper()