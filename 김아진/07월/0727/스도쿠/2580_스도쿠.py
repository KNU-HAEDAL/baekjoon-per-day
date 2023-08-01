import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(9)]
zero = []

def is_possible(r, c, num):
    if num in graph[r]:
        return False

    for i in range(9):
        if graph[i][c] == num:
            return False
    
    s_i = (r//3) * 3
    s_j = (c//3) * 3
    for i in range(3):
        for j in range(3):
            if num == graph[s_i + i][s_j + j]:
                return False

    return True

def sudoku(depth):
    if depth == len(zero):
        return True
    i, j = zero[depth]
    for k in range(1, 10):
        if is_possible(i, j, k):
            graph[i][j] = k
            flag = sudoku(depth + 1)
            if flag:
                return True
            graph[i][j] = 0
    return False

for i in range(9):
    for j in range(9):
        if not graph[i][j]:
            zero.append((i,j))

sudoku(0)

for i in range(9):
    print(*graph[i], ' ')