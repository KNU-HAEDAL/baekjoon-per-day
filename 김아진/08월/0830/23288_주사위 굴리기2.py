import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dice = [1, 2, 3, 4, 5, 6]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def roll_dice(x, y, d):
    x, y = x + dx[d], y + dy[d]
    if x < 0 or y < 0 or x >= n or y >= m:
        d = (d + 2) % 4
        x, y = x + dx[d]*2, y + dy[d]*2
    
    if d == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif d == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif d == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

    return x, y, d


def get_point(x, y, b):
    queue = deque([(x,y)])
    visited = [[False]*m for _ in range(n)]
    visited[x][y] = True
    count = 0

    while queue:
        x, y = queue.popleft()
        count += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == b:
                queue.append((nx,ny))
                visited[nx][ny] = True
    
    return count*b

def determine_direction(x, y, d):
    a, b = dice[5], board[x][y]
    if a > b:
        d = (d + 1) % 4
    elif a < b:
        d = (d - 1) % 4
    
    return d

point = 0
x, y, d = 0, 0, 0
for _ in range(k):
    x, y, d = roll_dice(x, y, d)
    point += get_point(x, y, board[x][y])
    d = determine_direction(x, y, d)

print(point)