import numpy as np

'''0 means the cells where no value is assigned'''
grid = [[0, 0, 6, 0, 3, 0, 2, 0, 8],
        [7, 8, 1, 0, 2, 0, 0, 0, 4],
        [0, 9, 2, 7, 8, 4, 1, 0, 0],
        [1, 0, 0, 2, 0, 0, 0, 0, 6],
        [0, 0, 8, 0, 0, 5, 0, 1, 0],
        [0, 2, 0, 6, 1, 0, 0, 4, 0],
        [8, 0, 0, 4, 0, 0, 0, 0, 1],
        [0, 0, 5, 0, 6, 0, 4, 8, 0],
        [9, 1, 4, 0, 0, 2, 6, 5, 3]]


# print(np.matrix(grid))


def possible(row, col, num):
    global grid

    # Is number present in the row
    for i in range(0, 9):
        if grid[row][i] == num:
            return False

    # Is number present in the column
    for i in range(0, 9):
        if grid[i][col] == num:
            return False

    # Is number present in the square
    x0 = (col // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == num:
                return False
    return True


def print_board(bo):
    for i in range(
            len(bo)):  # for loop iterating through each row.  'i' is the row, and 'j' is each value in each row.
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(bo[0])):  # iterating through each column of each row.
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(bo[i][j], end=" ")


count = 0


def solve_sudoku():
    global count
    global grid
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for num in range(1, 10):
                    if possible(row, column, num):
                        grid[row][column] = num
                        solve_sudoku()
                        grid[row][column] = 0
                return
    print_board(grid)
    count += 1
    print(f"Possible Solution Number:  {count}")
    print(f"======================================================")


solve_sudoku()
