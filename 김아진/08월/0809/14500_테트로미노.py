import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0

def dfs(x, y, depth, sum_n):
    global answer
    if depth == 4:
        answer = max(answer, sum_n)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, sum_n + board[nx][ny])
            visited[nx][ny] = False

edx = [(-1, 0, 0), (1, 0, 0), (1, 1, 2), (1, 1, 2)]
edy = [(1, 1, 2), (1, 1, 2), (1, 0, 0), (-1, 0, 0)]
def extra(x, y):
    global answer
    for i in range(4):
        sum_n = board[x][y]
        for j in range(3):
            nx, ny = x + edx[i][j], y + edy[i][j]
            if 0<=nx<n and 0<=ny<m:
                sum_n += board[nx][ny]
        answer = max(answer, sum_n)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

        extra(i,j)

print(answer)