import sys, copy
input = sys.stdin.readline
from itertools import product
from collections import deque

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
answer = n * m

types = [
    [],
    [[0], [1], [2], [3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
    ]

cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= office[i][j] <= 5:
            cctv.append((i,j, office[i][j]))

def watch_cctv(graph, x, y, cur):
    for i in cur:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            if graph[nx][ny] == 6:
                break
            if graph[nx][ny] == 0:
                graph[nx][ny] = -1
            
def dfs(depth, graph):
    global answer
    if depth == len(cctv):
        corner = 0
        for j in graph:
            corner += j.count(0)
        answer = min(answer, corner)
        return
    x, y, t = cctv[depth]

    for i in types[t]:
        board = [c[:] for c in graph]
        watch_cctv(board, x,y,i)
        dfs(depth+1, board)

type_index = deque()
dfs(0, office)
print(answer)