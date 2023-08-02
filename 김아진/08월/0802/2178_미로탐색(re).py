import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
level = 0

def bfs(x, y):
    global level
    queue = deque([(x,y)])
    graph[x][y] += 1
    while queue:
        queue_size = len(queue)
        for _ in range(queue_size):
            x, y = queue.popleft()
            if x == n - 1 and y == m - 1:
                return
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] += 1
                    queue.append((nx,ny))
        level += 1

bfs(0,0)
print(level + 1)