import numpy as np

# A class to represent cages
class Cage:
    def __init__(self, cells, value):
        self.cells = cells
        self.value = value

# Check if the placement of a number in a cell is valid
def is_valid(num, row, col, sudoku, cages):
    # Check if the number is already in the row, column, or box
    if (num in sudoku[row]) or (num in [sudoku[i][col] for i in range(9)]) or \
            (num in [sudoku[i][j] for i in range(row - row % 3, row - row % 3 + 3) for j in range(col - col % 3, col - col % 3 + 3)]):
        return False

    # Check the number in the current cage
    for cage in cages:
        cells = [(cell // 10 - 1, cell % 10 - 1) for cell in cage.cells]
        if (row, col) in cells:
            current_sum = num  # Start with the number we're trying to place
            for cell in cells:
                r, c = cell
                if sudoku[r][c] != 0:
                    current_sum += sudoku[r][c]
            # Check if the sum exceeds the cage's value
            if current_sum > cage.value:
                return False
            # Check if this is the last cell to fill in the cage and the sum doesn't match the cage's value
            empty_cells = sum(1 for cell in cells if sudoku[cell[0]][cell[1]] == 0)
            if empty_cells == 1 and current_sum != cage.value:
                return False

    return True

# Least Constraining Value heuristic
def lcv_values(row, col, sudoku, cages):
    values = []
    for num in range(1, 10):
        if is_valid(num, row, col, sudoku, cages):
            count = 0
            for i in range(9):
                if is_valid(num, row, col, sudoku, cages):
                    count += 1
            values.append((num, count))
    return sorted(values, key=lambda x: x[1])

# Least Remaining Values heuristic
def lrv_cells(sudoku, cages):
    empty_cells = []
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                count = sum(1 for num in range(1, 10) if is_valid(num, row, col, sudoku, cages))
                empty_cells.append(((row, col), count))
    return sorted(empty_cells, key=lambda x: x[1])

def solve_sudoku_with_heuristics(sudoku, cages):
    empty_cells = lrv_cells(sudoku, cages)
    if not empty_cells:
        return True

    (row, col), _ = empty_cells[0]
    values = lcv_values(row, col, sudoku, cages)

    for num, _ in values:
        if is_valid(num, row, col, sudoku, cages):
            sudoku[row][col] = num
            if solve_sudoku_with_heuristics(sudoku, cages):
                return True
            sudoku[row][col] = 0

    return False

def main():
    sudoku = []
    for _ in range(9):
        row_input = input().strip().split()
        sudoku.append([int(num) for num in row_input])

    # Input cages
    num_cages = int(input())
    cages = []
    for _ in range(num_cages):
        data = input("").split(" > ")
        cells = list(map(int, data[0].split()))
        value = int(data[1])
        cages.append(Cage(cells, value))

    # Solve Sudoku with LCV and LRV heuristics
    if solve_sudoku_with_heuristics(sudoku, cages):
        print(np.matrix(sudoku))
    else:
        print("not solvable")

if __name__ == "__main__":
    main()
