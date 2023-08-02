import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
queue = deque()

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))
bfs()

answer = 0
for i in graph:
    if 0 in i:
        answer = 0
        break
    answer = max(max(i), answer)
print(answer - 1)