import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
check = [[False]*m for _ in range(n)] # cycle 확인용
direction = ['D', 'U', 'L', 'R']
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
safe = 0

def pipe(x,y,):
    global safe
    
    if visited[x][y] == True:
        if check[x][y] == False:
            safe += 1
        return
    
    visited[x][y] = True
    index = direction.index(graph[x][y])
    nx, ny = x + dx[index], y + dy[index]
    pipe(nx, ny)
    check[x][y] = True

for i in range(n):
    for j in range(m):
            if visited[i][j] == False:
                pipe(i,j)
            
print(safe)