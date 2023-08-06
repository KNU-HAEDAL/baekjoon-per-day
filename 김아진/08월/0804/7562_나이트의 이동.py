import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
dx = [1,2,-1,-2,1,2,-1,-2]
dy = [2,1,2,1,-2,-1,-2,-1]

def bfs(x,y,ex,ey):
    queue = deque([(x,y)])
    visited = [[0]*n for _ in range(n)]
    
    while queue:
        x, y = queue.popleft()
        if x == ex and y == ey:
            return visited[ex][ey]
        for i in range(8):
            nx,ny = x + dx[i], y + dy[i]
            if (0<=nx<n and 0<=ny<n) and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

while t:
    n = int(input())
    start_x, start_y = map(int,input().split())
    finish_x, finish_y = map(int,input().split())
    print(bfs(start_x, start_y, finish_x, finish_y))
    t -= 1