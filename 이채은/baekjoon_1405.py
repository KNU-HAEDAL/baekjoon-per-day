import sys
input = sys.stdin.readline

N,e,w,s,n = map(int,input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
data = [e,w,s,n]
graph = [[0] * (2*N+1) for _ in range(2*N+1)]
result = 0

def dfs(x,y,prob,cnt):
    global result
    if cnt == N:
        result += prob
        return
    nowprob = prob
    graph[x][y] = 1
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx < (2*N+1) and 0 <= newy < (2*N+1):
            if graph[newx][newy] == 1:
                continue
            else:
                dfs(newx,newy,nowprob*(data[i]/100),cnt+1)
                graph[newx][newy] = 0

dfs(N,N,1,0)
print(result)
