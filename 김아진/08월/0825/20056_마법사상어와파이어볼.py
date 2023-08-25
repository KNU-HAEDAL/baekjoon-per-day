import sys, copy
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append((m,s,d))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move_fireball(x, y, fireball):
    m, s, d = fireball
    nx, ny = (x + dx[d]*s) % n, (y + dy[d]*s) % n
    temp_board[nx][ny].append((m,s,d))

def divide_fireball(i,j):
    m, s, d_even, d_odd = 0, 0, 0, 0
    cur_board = board[i][j]
    for fireball in cur_board:
        m += fireball[0]
        s += fireball[1]
        if fireball[2] % 2 == 0:
            d_odd += 1
        else:
            d_even += 1
            
    m, s = m // 5, s // len(cur_board)
    if d_odd == len(cur_board) or d_even == len(cur_board):
        p = 0
    else:
        p = 1

    board[i][j] = []
    if m:
        for k in range(4):
            board[i][j].append((m,s,k*2+p))
        
for _ in range(k):
    # 파이어볼 이동하기
    temp_board = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                for fireball in board[i][j]:
                    move_fireball(i, j, fireball)
    board = copy.deepcopy(temp_board)

    # 파이어볼 4분할하기
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) > 1:
                divide_fireball(i,j)

# 질량 구하기
mass = 0
for i in range(n):
    for j in range(n):
        if board[i][j]:
            for fireball in board[i][j]:
                mass += fireball[0]
print(mass)
