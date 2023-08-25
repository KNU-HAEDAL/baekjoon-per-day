import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def move_sand(x, y, d):
    global out_sand
    if y < 0:
        return

    sand_sum, sand = 0, board[x][y]
    for tx, ty, tr in d:
        nx, ny = x + tx, y + ty

        if tr == 0:
            cur_sand = sand - sand_sum
        else:
            cur_sand = int(sand * tr)
            sand_sum += cur_sand

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            out_sand += cur_sand
        else:
            board[nx][ny] += cur_sand

# 모래 이동 방향
left = [(-2,0,0.02), (-1,-1,0.1), (-1,0,0.07), (-1,1,0.01), (0,-2,0.05), (1,-1,0.1), (1,0,0.07), (1,1,0.01), (2,0,0.02), (0, -1, 0)]
right = [(x,-y,r) for x, y, r in left]
down = [(-y, x, r) for x, y, r in left]
up = [(y, x, r) for x, y, r, in left]

out_sand = 0
direction = {0: left, 1: down, 2: right, 3: up}

time = 0
x, y = n // 2, n // 2
for i in range(2*n-1):
    d = i % 4

    if d % 2 == 0:
        time += 1

    for _ in range(time):
        nx, ny = x + dx[d], y + dy[d]
        move_sand(nx, ny, direction[d])
        x, y = nx, ny

print(out_sand)