import sys
input = sys.stdin.readline

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
horse_in_board = [[[] for _ in range(n)] for _ in range(n)]
horses = []
for i in range(k):
    x, y, d = map(int, input().split())
    horse_in_board[x-1][y-1].append((i))
    horses.append([x-1,y-1,d-1])
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move_horses():
    for i in range(len(horses)):
        x, y, d = horses[i]
        nx, ny = x + dx[d], y + dy[d]
        
        # 경계 벗어나거나, 파란색이면
        if (0>nx or 0>ny or nx>=n or ny>=n) or (board[nx][ny] == 2):
            # 방향 바꾸기
            if d % 2 == 0:
                d += 1
            else:
                d -= 1
            horses[i][2] = d
            # 한 칸 이동하기
            nx, ny = x + dx[d], y + dy[d]
        
        # 또 경계 벗어나거나, 파란색이면
        if (0>nx or 0>ny or nx>=n or ny>=n) or (board[nx][ny] == 2):
            # 가만히 있기
            continue
        
        # 현재 말 위에 있는 말 모두 옮기기
        cur_horse = []
        for index, num in enumerate(horse_in_board[x][y]):
            if num == i:
                cur_horse.extend(horse_in_board[x][y][index:])
                horse_in_board[x][y] = horse_in_board[x][y][:index]
                break

        # 빨간색이면 뒤집기
        if board[nx][ny] == 1:
            cur_horse.reverse()
        
        # 말 위치 업데이트
        for index in cur_horse:
            horses[index][0] = nx
            horses[index][1] = ny
        # 말있는 보드 업데이트
        horse_in_board[nx][ny].extend(cur_horse)

        # 말 4개이상 쌓여있으면 종료
        if len(horse_in_board[nx][ny]) >= 4:
            return False
    return True

t = 0
while True:
    if t > 1000:
        t = -1
        break
    t += 1
    if not move_horses():
        break
print(t)