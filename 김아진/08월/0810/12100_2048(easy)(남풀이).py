import sys, copy
input = sys.stdin.readline
from collections import deque
from itertools import product

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

def merge(x, y, moves):
    dx, dy = moves
    while queue:
        num = queue.popleft()
        if board[x][y] == 0:
            board[x][y] = num
        elif board[x][y] == num:
            board[x][y] *= 2
            x, y = x + dx, y + dy
        else:
            x, y = x + dx, y + dy
            board[x][y] = num

def select_direction(cur_d):
    if cur_d == 0:
        for j in range(n):
            for i in range(n-1, -1, -1):
                if board[i][j]:
                    queue.append(board[i][j])
                    board[i][j] = 0
            merge(n-1, j, (-1, 0))
    elif cur_d == 1:
        for i in range(n):
            for j in range(n-1, -1, -1):
                if board[i][j]:
                    queue.append(board[i][j])
                    board[i][j] = 0
            merge(i, n-1, (0, -1))
    elif cur_d == 2:
        for j in range(n):
            for i in range(n):
                if board[i][j]:
                    queue.append(board[i][j])
                    board[i][j] = 0
            merge(0, j, (1, 0))
    else:
        for i in range(n):
            for j in range(n):
                if board[i][j]:
                    queue.append(board[i][j])
                    board[i][j] = 0
            merge(i, 0, (0, 1))

max_num = 0
def move_board(depth):
    global board, max_num
    if depth == 5:
        max_num = max(max_num, max(map(max, board)))
        return
    temp = copy.deepcopy(board)
    for i in range(4):
        board = copy.deepcopy(temp)
        select_direction(i)
        move_board(depth + 1)
        
move_board(0)
print(max_num)