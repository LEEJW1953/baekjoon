import sys

input = sys.stdin.readline


def dfs(count):
    if count == len(point):
        for i in range(9):
            print("".join(list(map(str, sudoku[i]))))
        exit(0)
    for i in range(1, 10):
        if (
            hor(i, point[count][1])
            and ver(i, point[count][0])
            and square(i, point[count][0], point[count][1])
        ):
            sudoku[point[count][1]][point[count][0]] = i
            dfs(count + 1)
            sudoku[point[count][1]][point[count][0]] = 0


def hor(num, y):
    for i in range(9):
        if sudoku[y][i] == num:
            return False
    return True


def ver(num, x):
    for i in range(9):
        if sudoku[i][x] == num:
            return False
    return True


def square(num, x, y):
    for i in range(3 * (y // 3), 3 * (y // 3) + 3):
        for j in range(3 * (x // 3), 3 * (x // 3) + 3):
            if sudoku[i][j] == num:
                return False
    return True


sudoku = [list(map(int, input().strip())) for _ in range(9)]
point = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            point.append([j, i])
dfs(0)