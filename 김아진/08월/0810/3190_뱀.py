import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
board = [[0]* (n+1) for _ in range(n+1)]

for _ in range(k): # 사과 위치 저장
    x, y = map(int, input().split())
    board[x][y] = 2

l = int(input())
direction = {}
for _ in range(l): # 방향 변환 정보 저장
    x, c = input().split()
    direction[int(x)] = c

# 초기값 세팅
x, y = 1, 1
board[x][y] = 1
dx, dy = 0, 1
cur_time = 0
snake = [(x,y)]

while True:
    # 시간되면 방향 바꾸기
    if cur_time in direction:
        if direction[cur_time] == 'L':
            dx, dy = -1 * dy, dx
        else:
            dx, dy = dy, -1 * dx

    # 한 칸씩 이동하기
    nx, ny = x + dx, y + dy

    # 맵 밖에 나가면 탈출
    if nx <= 0 or nx > n or ny <= 0 or ny > n:
        break
    # 뱀에 닿으면 탈출
    if board[nx][ny] == 1:
        break

    # 사과 없으면 꼬리 이동
    if board[nx][ny] != 2:
        px, py = snake.pop(0)
        board[px][py] = 0
        
    # 머리 이동
    board[nx][ny] = 1
    snake.append((nx, ny))
    
    # 1초 증가
    cur_time += 1
    x, y = nx, ny

print(cur_time + 1)