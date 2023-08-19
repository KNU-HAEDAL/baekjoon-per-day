import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def spread_dust(x, y, d):
    count = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if room[nx][ny] == -1:
            continue
        count += 1
        room[nx][ny] += d // 5
    room[x][y] += d - (d//5)*count

def circulate_air():
    dust_list = [[] for _ in range(4)]
    # ↓
    j = 0
    for i in range(air[0]):
        dust_list[0].append((i,j, room[i][j]))
    j = c - 1
    for i in range(air[1], r-1):
        dust_list[0].append((i,j, room[i][j]))
    # ->
    for i in air:
        for j in range(1, c-1):
            dust_list[1].append((i,j, room[i][j]))
        room[i][1] = 0
    # ↑
    j = c - 1
    for i in range(1, air[0]+1):
        dust_list[2].append((i,j, room[i][j]))
    j = 0
    for i in range(air[1]+1, r):
        dust_list[2].append((i,j, room[i][j]))
    # <-
    for i in [0, r-1]:
        for j in range(1, c):
            dust_list[3].append((i,j, room[i][j]))
    
    # 먼지 이동하고 청정기 세팅다시하기
    for i in range(4):
        for x, y, d in dust_list[i]:
            nx, ny = x + dx[i], y + dy[i]
            room[nx][ny] = d
    room[air[0]][0], room[air[1]][0] = -1, -1

# 공기청정기 위치
air = []
for i in range(r):
    for j in range(c):
        if room[i][j] == -1:
            air.append(i)

for _ in range(t):
    dust = []
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                dust.append((i,j, room[i][j]))
                room[i][j] = 0

    for i,j,d in dust:
        spread_dust(i,j,d)

    circulate_air()

answer = sum(sum(room[i]) for i in range(r)) + 2
print(answer)