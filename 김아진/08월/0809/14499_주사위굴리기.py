import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

dice = [[0]*3 for _ in range(4)]
dice = [0]*6
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for i in order:
    nx, ny = x + dx[i], y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
     
    # 주사위 굴리기
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if i == 1: # 동쪽
        dice = [f, b, e, d, a, c]
    elif i == 2: # 서쪽
        dice = [e, b, f, d, c, a]
    elif i == 3: #북쪽
        dice = [d, a, b, c, e, f]
    else:
        dice = [b, c, d, a, e, f]
    
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[2] # 바닥면
    else:
        dice[2] = graph[nx][ny]
        graph[nx][ny] = 0

    print(dice[0]) # 윗 면
    x, y = nx, ny