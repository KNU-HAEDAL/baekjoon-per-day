import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(select_virus):
    time = 0
    queue = deque()
    visited = [[-1]*n for _ in range(n)]
    
    for i,j in select_virus:
        queue.append((i,j))
        visited[i][j] = 0
   
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            if visited[nx][ny] != -1:
                continue
            if lab[nx][ny] == 1:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
            
            if lab[nx][ny] == 0:
                time = max(time, visited[nx][ny])

    for i in range(n):
        for j in range(n):
            if lab[i][j] != 0:
                continue
            if visited[i][j] == -1:
                return -1
    return time

virus = []
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus.append((i,j))

answer = sys.maxsize
for select_virus in combinations(virus, m):
    time = bfs(select_virus)
    if time != -1:
        answer = min(answer, time)

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)