import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
queue = deque()
answer = 0

def bfs():
    global answer
    while queue:
        queue_size = len(queue)
        for _ in range(queue_size):
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx,ny))
        answer += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

bfs()

for i in graph:
    if 0 in i:
        answer = 0
        break
print(answer - 1)