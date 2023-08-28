import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappush, heappop

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def number_of_colors(color, start_x, start_y):
    queue = deque([(start_x, start_y)])
    num, rainbow = 0, 0
    visited_zero = [[False]*n for _ in range(n)]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if board[nx][ny] == 0 and not visited_zero[nx][ny]:
                rainbow += 1
                visited_zero[nx][ny] = True
            elif board[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = True
            else:
                continue
            queue.append((nx, ny))
            num += 1

    # 크기 같다면 추가
    if -max_color[0][0] == num:
        heappush(max_color, (-num, -rainbow, -start_x, -start_y, color))
    # 크기 더 크면 새로 만들기
    elif -max_color[0][0] < num:
        while max_color:
            heappop(max_color)
        heappush(max_color, (-num, -rainbow, -start_x, -start_y, color))

def delete_block(color, x, y):
    queue = deque([(x,y)])
    visited_delete = [[False]*n for _ in range(n)]
    board[x][y] = -9
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited_delete[nx][ny]:
                continue
            if board[nx][ny] == color or board[nx][ny] == 0:
                visited_delete[nx][ny] = True
                queue.append((nx, ny))
                board[nx][ny] = -9

def gravity():
    for c in range(n):
        k = n
        for i in range(n-2, -1, -1):
            if board[i][c] == -1:
                k = i
                continue
            for r in range(i+1, k):
                if board[r][c] == -9:
                    board[r][c] = board[r-1][c]
                    board[r-1][c] = -9
                    continue

point = 0
while True:
    max_color = [] # 크기, 무지개, i, j, 색
    heappush(max_color, (-1, -1, -1, -1, -1))
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            if 1 <= board[i][j] <= m:
                number_of_colors(board[i][j], i, j)
    
    if -max_color[0][0] < 2:
        break

    size, _, x, y, color = max_color[0]
    point += (-size)**2
    delete_block(color, -x, -y)

    gravity()

    board = list(map(list, zip(*board)))[::-1]

    gravity()

print(point)