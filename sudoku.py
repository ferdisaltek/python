def sudoku(puzzle):
    def vaild(puzzle):
        for m in range(9):
            if puzzle[m][j]==puzzle[i][j] and m!= i:
                return False
        for n in range(9):
            if puzzle[i][n]==puzzle[i][j] and n!= j:
                return False
        for m in range(3):
            for n in range(3):
                if puzzle[int(i/3)*3+m][int(j/3)*3+n]==puzzle[i][j] and m!= i and n!= j and int(i/3)*3+m != i and int(j/3)*3+n!=j:
                    return False
        return True
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for d in range(1,10):
                    puzzle[i][j] = d
                    if vaild(puzzle):
                        if sudoku(puzzle):
                            return puzzle
                        else:
                            puzzle[i][j] = 0
                    else:
                        puzzle[i][j] = 0
                return False 
    return puzzle

#----------------------------------------------------------------------

def sudoku(puzzle):
    while 0 in [number for row in puzzle for number in row]:
        for row in range(len(puzzle)):
            for i in range(len(puzzle)):
                if puzzle[row][i] == 0:
                    numbers = []
                    row_numbers = puzzle[row]
                    column_numbers = [e[i] for e in puzzle]
                    grid_numbers = [h for t in [g[(i//3)*3:(i//3)*3+3] for g in puzzle[(row//3)*3:(row//3)*3+3]] for h in t]
                    check_numbers = set(row_numbers+column_numbers+grid_numbers)
                    for number in range(1, 10):
                        if number not in check_numbers:
                            numbers.append(number)
                    if len(numbers) == 1:
                        puzzle[row][i] = numbers[0]
    return puzzle