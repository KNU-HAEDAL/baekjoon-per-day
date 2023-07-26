import sys
input = sys.stdin.readline

from collections import deque

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
queue = set([(0,0,graph[0][0])])
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
answer = 0

while queue:
    x, y, s = queue.pop()
    answer = max(answer, len(s))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in s:
            queue.add((nx, ny, s + graph[nx][ny]))

print(answer)
