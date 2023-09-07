# Create a Battleship program using a 2D array

import random

# Declare global variables
grid = []
grid_size = 10
num_of_ships = 5

# Draw board using 2D grid array with labels for rows and columns
def drawBoard(arr):
    print("|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |")
    for i in range(len(arr)):
        print("| " + str(i) + " |", end="")
        for j in range(len(arr[i])):    
            print(" " + arr[i][j] + " |", end="")
        print("\n")

# Create the 2D array for the board by assigning each element as '.' for empty spaces and 'S' for ships
def setupBoard():
    # Create 10 x 10 array of dots that represent empty spaces
    rows, col = (grid_size, grid_size)
    global grid 
    for i in range(rows):
        column = []
        for j in range(col):
            column.append(".")
        grid.append(column)
    # Assign some elements to be ships
    for x in range(num_of_ships):
        while True:
            randomRow = random.randint(0, grid_size - 1)
            randomCol = random.randint(0, grid_size - 1)
            # Ensure that ships get placed in 5 unique places
            if grid[randomRow][randomCol] != 'S':
                grid[randomRow][randomCol] = 'S'
                break
    # return grid for unit test
    return grid

# Check if game is over by checking if all ships have been sunk    
def isGameOver(arr):
    sunk_ships = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'X':
                sunk_ships = sunk_ships + 1
    return sunk_ships == num_of_ships

# Check if the user's guess hit a ship or missed
def checkHitOrMiss(row, col, arr):
    #global grid
    if arr[row][col] == 'S':
        arr[row][col] = 'X'
        print("HIT")
    else:
        arr[row][col] = 'O'
        print("MISS")

# Main function creates the game for user to play
def main():
    # Create board and output it to user
    setupBoard()
    drawBoard(grid)

    # Continue to ask user for guess, check if they hit a ship, and output the board for the user until all ships are sunk
    while not isGameOver(grid):
        try:
            rowGuess = eval(input("Enter row:    "))
            colGuess = eval(input("Enter column: "))
            checkHitOrMiss(rowGuess, colGuess, grid)
            drawBoard(grid)
        except IndexError:
            print("Please enter integers between 0 and 9.")
        except NameError:
            print("Please enter only integers.")

    print("GAME OVER")

main()






