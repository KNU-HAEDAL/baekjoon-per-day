import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
start = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
size = 2
eat = 0

def bfs(x, y):
    global size, eat
    heap = []
    heappush(heap, (0,x,y))
    graph[x][y] = 0
    visited = [[0]*n for _ in range(n)]
    while heap:
        depth, x, y = heappop(heap)
        # 먹기 가능
        if graph[x][y] != 0 and graph[x][y] < size:
            eat += 1
            graph[x][y] = 0
            start.append((x,y))
            # 증가 가능
            if eat == size:
                eat = 0
                size += 1
            return visited[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not(0<=nx<n) or not(0<=ny<n):
                continue
            if visited[nx][ny] or graph[nx][ny] > size:
                continue
            # 이동 가능
            visited[nx][ny] = depth + 1
            heappush(heap, (visited[nx][ny], nx, ny))
    return 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            start.append((i,j))

time = 0
for start_index in start:
    x, y = start_index
    time += bfs(x,y)
print(time)
