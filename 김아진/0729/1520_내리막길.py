import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
dx = [1, 0, 0,-1]
dy = [0, 1, -1,0]

def go_down(i,j):
    if i == n-1 and j == m-1:
        return 1
    
    if dp[i][j] == -1:
        dp[i][j] = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if (nx < 0 or n <= nx) or (ny < 0 or m <= ny):
                continue
            if graph[i][j] > graph[nx][ny]:
                dp[i][j] += go_down(nx,ny)
        
    return dp[i][j]

print(go_down(0,0))