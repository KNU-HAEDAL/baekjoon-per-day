import sys, copy
input = sys.stdin.readline

r, c, m = map(int, input().split())
sharks = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    sharks[x-1][y-1].append((s,d-1,z))
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def next_shark_d(x,y,s,d):
    if d//2 == 0:
        cycle = (r-1)*2
        if d % 2 == 0:
            s += cycle - x
        else:
            s += x
        s %= cycle
        if s >= r:
            return (cycle - s, y, 0)
        return (s, y, 1)
    else:
        cycle = (c-1)*2
        if d % 2 == 1:
            s += cycle - y
        else:
            s += y
        s %= cycle
        if s >= c:
            return (x, cycle - s, 3)
        return (x, s, 2)
    
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