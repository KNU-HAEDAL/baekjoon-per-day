import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x, y, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

while True:
    # 현재 위치 청소하기
    if room[x][y] == 0:
        room[x][y] = 2
    
    # 주변 위치 돌아보기
    check = False
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if room[nx][ny] == 0:
            check = True
    
    # 주변 다 청소되어 있음
    if check == False:
        nx, ny = x - dx[d], y - dy[d]
        # 후진 불가능
        if room[nx][ny] == 1:
            break
        # 현재 방향 업데이트
        x, y = nx, ny
    # 주변 청소 안되어있음
    else:
        # 반시계 방향으로 90도 회전하기
        for i in range(1, 5):
            nx, ny = x + dx[d-i], y + dy[d-i]
            if room[nx][ny] != 0:
                continue
            # 방 청소하기
            room[nx][ny] = 2
            # 상태 업데이트하기
            d = d - i
            if d < 0:
                d += 4
            x, y = nx, ny
            break

answer = 0
for line in room:
    answer += line.count(2)

print(answer)