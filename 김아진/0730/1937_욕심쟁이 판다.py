import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[1]*n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = 0

def bamboo(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 > nx or nx >= n or 0 > ny or ny >=n:
            continue
        if graph[x][y] < graph[nx][ny]:
            dp[nx][ny] = max(dp[x][y] + 1, dp[nx][ny])

sort_list = []
for i in range(n):
    for j in range(n):
        sort_list.append((graph[i][j],(i,j)))

sort_list.sort()

for value, (i, j) in sort_list:
    bamboo(i, j)

for i in range(n):
    for j in range(n):
        answer = max(answer, dp[i][j])
    
print(answer)