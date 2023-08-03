import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

m, n, k = map(int, input().split())
point = []
graph = [[0]*m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if not(0<=x<n) or not(0<=y<m) or graph[x][y]:
        return 0
    graph[x][y] = 1
    return 1 + dfs(x+1, y) + dfs(x, y+1) + dfs(x-1, y) + dfs(x, y - 1)

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = -1

area = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            area.append(dfs(i,j))

print(len(area))
area.sort()
print(*area)