from sys import stdin
sudoku = [list(map(int, stdin.readline().split())) for _ in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def possibleSudoku(ai, aj):
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if sudoku[ai][i] in check:
            check.remove(sudoku[ai][i])
        if sudoku[i][aj] in check:
            check.remove(sudoku[i][aj])
    for i in range(ai//3*3, ai//3*3+3):
        for j in range(aj//3*3, aj//3*3+3):
            if sudoku[i][j] in check:
                check.remove(sudoku[i][j])
    return check


def calSudoku(arg):
    if len(zero) == arg:
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end='')
                if j != 8:
                    print(' ', end='')
            print()
        exit(0)

    ai, aj = zero[arg]
    tmpList = possibleSudoku(ai, aj)
    for i in tmpList:
        sudoku[ai][aj] = i
        calSudoku(arg+1)
        sudoku[ai][aj] = 0

calSudoku(0)
