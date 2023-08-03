import sys, copy
input = sys.stdin.readline
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
blank_index = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0

def make_walls():
    global answer
    three_walls = list(combinations(blank_index,3))
    for wall in three_walls:
        virus_graph = copy.deepcopy(graph)
        for i in range(3):
            x, y = wall[i]
            virus_graph[x][y] = 1
        spread_virus(virus_graph)
        blank_cnt = 0
        for line in virus_graph:
            blank_cnt += line.count(0)
        answer = max(blank_cnt, answer)

def spread_virus(graph):
    queue = deque([])
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i,j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx,ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank_index.append((i,j))
make_walls()
print(answer)