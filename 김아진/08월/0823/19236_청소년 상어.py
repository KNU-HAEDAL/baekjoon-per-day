import sys, copy
input = sys.stdin.readline
from collections import deque

board = [[[] for _ in range(4)] for _ in range(4)]
for i in range(4):
    row = list(map(int,input().split()))
    fish = []
    for j in range(4):
        fish.append([row[2*j], row[2*j+1]-1])
    board[i] = fish

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
answer = 0

def is_fish_here(board, fish):
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == fish:
                x, y = i, j
                return x, y
    return -1, -1

def move_fish(board, sx, sy):
    for fish in range(1, 17):
        x, y = is_fish_here(board, fish)
        if x == -1 and y == -1:
            continue

        d = board[x][y][1]
        for i in range(8):
            nd = (d + i) % 8
            nx, ny = x + dx[nd], y + dy[nd]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue
            if nx == sx and ny == sy:
                continue
            board[x][y][1] = nd
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
            break

def dfs(sx, sy, score, board):
    global answer
    
    # 물고기 잡아먹기
    score += board[sx][sy][0]
    answer = max(answer, score)
    board[sx][sy][0] = 0

    # 물고기 움직이기
    move_fish(board, sx, sy)
    
    # 상어 움직이기
    sd = board[sx][sy][1]
    for i in range(1, 4):
        nx, ny = sx + dx[sd]*i, sy + dy[sd]*i
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            continue
        if board[nx][ny][0] == 0:
            continue
        dfs(nx, ny, score, copy.deepcopy(board))

dfs(0,0,0,board)
print(answer)