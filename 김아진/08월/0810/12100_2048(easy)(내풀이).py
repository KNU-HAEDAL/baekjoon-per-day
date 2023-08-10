import sys, copy
input = sys.stdin.readline
from itertools import product

n = int(input())
origin = [list(map(int, input().split())) for _ in range(n)]
direction = ['U', 'L', 'D', 'R']
dlist = list(product(direction, repeat=5))

def move_up():
    for c in range(n):
        for i in range(1,n):
            for r in range(i-1, -1, -1):
                if merged[r][c]:
                    break
                if board[r][c] == 0:
                    board[r][c] = board[r+1][c]
                    board[r+1][c] = 0
                    continue

                if board[r][c] == board[r+1][c]:
                    merged[r][c] = True
                    board[r][c] *= 2
                    board[r+1][c] = 0
                break

def move_left():
    for r in range(n):
        for i in range(1, n):
            for c in range(i-1, -1, -1):
                if merged[r][c]:
                    break
                if board[r][c] == 0:
                    board[r][c] = board[r][c+1]
                    board[r][c+1] = 0
                    continue

                if board[r][c] == board[r][c+1]:
                    merged[r][c] = True
                    board[r][c] *= 2
                    board[r][c+1] = 0
                break

def move_down():
    for c in range(n):
        for i in range(n-2, -1, -1):
            for r in range(i+1, n):
                if merged[r][c]:
                    break
                if board[r][c] == 0:
                    board[r][c] = board[r-1][c]
                    board[r-1][c] = 0
                    continue

                if board[r][c] == board[r-1][c]:
                    merged[r][c] = True
                    board[r][c] *= 2
                    board[r-1][c] = 0
                break

def move_right():
    for r in range(n):
        for i in range(n-2, -1, -1):
            for c in range(i+1, n):
                if merged[r][c]:
                    break
                if board[r][c] == 0:
                    board[r][c] = board[r][c-1]
                    board[r][c-1] = 0
                    continue

                if board[r][c] == board[r][c-1]:
                    merged[r][c] = True
                    board[r][c] *= 2
                    board[r][c-1] = 0
                break
max_num = 0
for d in dlist:
    board = copy.deepcopy(origin)
    
    for i in range(5):
        merged = [[False]*n for _ in range(n)]
        cur_d = d[i]
        if cur_d == 'U':
            move_up()
        elif cur_d == 'L':
            move_left()
        elif cur_d == 'D':
            move_down()
        else:
            move_right()

    max_num = max(max_num, max(map(max, board)))

print(max_num)