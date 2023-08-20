import sys, copy
input = sys.stdin.readline

r, c, m = map(int, input().split())
sharks = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    sharks[x-1][y-1].append((s,d-1,z))
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def next_shark_d(x, y, s, d):
    for _ in range(s):
        x, y = x + dx[d], y + dy[d]
        # 경계값을 벗어나면 방향 바꿔주고 안으로 위치 이동하기
        if ((0 > x or x >= r) and (d//2 == 0)) or ((0 > y or y >= c) and (d//2 == 1)):
            if d % 2 == 1:
                d -= 1
            else:
                d += 1
            x, y = x + dx[d]*2, y + dy[d]*2
    return x, y, d

def move_sharks():
    temp_sharks = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if sharks[i][j]:
                s, d, z = sharks[i][j][0]
                x, y, d = next_shark_d(i,j,s,d)
                temp_sharks[x][y].append((s,d,z))
    for i in range(r):
        for j in range(c):
            sharks[i][j] = temp_sharks[i][j]

def eat_sharks():
    for i in range(r):
        for j in range(c):
            if len(sharks[i][j]) > 1:
                # 크기가 가장 큰 상어만 살아남기
                sharks[i][j].sort(key=lambda x:x[2], reverse=True)
                sharks[i][j] = [(sharks[i][j][0])]

catch = 0
for king in range(c):
    # 낚시왕이 상어 잡기
    for i in range(r):
        if sharks[i][king]:
            _, _, z = sharks[i][king][0]
            catch += z
            sharks[i][king] = []
            break
    
    # 상어 이동하기
    move_sharks()

    # 상어 잡아먹기
    eat_sharks()

print(catch)