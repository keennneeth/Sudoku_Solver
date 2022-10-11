
from pprint import pprint


def find_empty_slot(puzzle): #First step, create function to find an empty slot on board that is not filled yet
                             #returns the index of the row & column

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r,c          #0-8, will find the next row/column that has '0', meaning it is not filled 

    return None, None               #will return none if the space is filled


def valid(puzzle, guess, row, col):

#if guessed number is a number already in the row then return false
    row_vals = puzzle[row]
    if guess in row_vals:
        return False


#checking if guessed nubmer is a number already in the column, returns false if it is
    col_vals = [puzzle[i][col] for i in range (9)]
    if guess in col_vals:
        return False



    row_start = (row // 3) * 3      #getting row/col value
    col_start = (col // 3) * 3

    for r in range (row_start, row_start + 3):      #+3 so it can iterate through each row
        for c in range (col_start, col_start + 3):  #+3 so it can iterate through each col
            if puzzle[r][c] == guess:
                return False

    return True





def solve_sudoku(puzzle):

    row, col = find_empty_slot(puzzle)

    if row is None: 
        return True

        #time to start finding the number that belongs in slot

    for guess in range (0, 9):         #make a guess from 1-9
                                        #recursively call this function until it makes correct guess
        if valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True


        puzzle[row][col] = 0

    return False

if __name__ == '__main__':
    board = [[3, 9, 0,  0, 5, 0,   0, 0, 0],
            [0, 0, 0,   2, 0, 0,   0, 0, 5],
            [0, 0, 0,   7, 1, 9,   0, 8, 0],

            [0, 5, 0,   0, 6, 8,   0, 0, 0],
            [2, 0, 6,   0, 0, 3,   0, 0, 0],
            [0, 0, 0,   0, 0, 0,   0, 0, 4],

            [5, 0, 0,   0, 0, 0,   0, 0, 0],
            [6, 7, 0,   1, 0, 5,   0, 4, 0],
            [1, 0, 9,   0, 0, 0,   2, 0, 0]
    ]
    print(solve_sudoku(board))
    pprint(board)
