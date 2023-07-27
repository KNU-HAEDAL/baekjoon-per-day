import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(9)]
row = [[0]*10 for _ in range(9)]
col = [[0]*10 for _ in range(9)]
square = [[0]*10 for _ in range(9)]
zero = []

def sudoku(depth):
    if depth == len(zero):
        return True
    i, j = zero[depth]
    for k in range(1, 10):
        if not(row[i][k] + col[j][k] + square[(i//3)*3 + (j//3)][k]):
            graph[i][j] = k
            row[i][k] = col[j][k] = square[(i//3)*3 + (j//3)][k] = 1
            flag = sudoku(depth + 1)
            if flag:
                return True
            row[i][k] = col[j][k] = square[(i//3)*3 + (j//3)][k] = 0
            graph[i][j] = 0
    return False

for i in range(9):
    for j in range(9):
        if graph[i][j]:
            k = graph[i][j]
            row[i][k] = col[j][k] = square[(i//3)*3 + (j//3)][k] = 1
        else:
            zero.append((i,j))

sudoku(0)

for i in range(9):
    print(*graph[i], ' ')