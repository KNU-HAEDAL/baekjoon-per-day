import sys, copy
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    queue = deque([(0,0,0)])
    visited[0][0][0] = 1

    while queue:
        x, y, is_break = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][is_break]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not(0<=nx<n) or not(0<=ny<m):
                continue
            
            if graph[nx][ny] == 1 and is_break == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            elif graph[nx][ny] == 0 and visited[nx][ny][is_break] == 0:
                visited[nx][ny][is_break] = visited[x][y][is_break] + 1
                queue.append((nx, ny, is_break))
    return -1

print(bfs())
