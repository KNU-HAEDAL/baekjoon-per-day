import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
shark = [[] for _ in range(m)]
for i in range(n):
    for j in range(n):
        if board[i][j]:
            shark[board[i][j]-1] = [i,j]
            board[i][j] = [board[i][j], k]

first_d = list(map(int, input().split()))
for i in range(m):
    shark[i].append(first_d[i])

priority = [[] for _ in range(m)]
for i in range(m):
    temp = []
    for j in range(4):
        temp.append(list(map(int, input().split())))
    priority[i].extend(temp)

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

def move_no_smell(num, cur_shark):
    x, y, d = cur_shark

    d_list = priority[num][d-1]
    for nd in d_list:
        nx, ny = x + dx[nd], y + dy[nd]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if board[nx][ny] == 0:
            return nx, ny, nd
    return -1, -1, -1

def move_my_smell(num, cur_shark):
    x, y, d = cur_shark
    
    d_list = priority[num][d-1]
    for nd in d_list:
        nx, ny = x + dx[nd], y + dy[nd]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if board[nx][ny][0] == num+1:
            return nx, ny, nd
    return -1, -1, -1

time = 0
while True:
    # 시간 초과
    if time > 1000:
        time = -1
        break

    # 상어 혼자 있음
    if shark.count(0) == m - 1:
        break

    check = [[0]*n for _ in range(n)]
    
    # 상어 이동하기
    for i in range(m):
        if shark[i]:
            # 냄새 없는 데로 이동하기
            nx, ny, nd = move_no_smell(i, shark[i])
            # 이동안했으면 내 냄새있는 곳으로 이동
            if nx == -1:
                nx, ny, nd = move_my_smell(i, shark[i])
            
            # 한 칸에 여러 상어 있으면 잡아먹기
            if check[nx][ny]:
                if i+1 > check[nx][ny]:
                    shark[i] = 0
                else:
                    shark[check[nx][ny]-1] = 0
                    check[nx][ny] = i + 1 
            else:
                shark[i] = [nx, ny, nd]
                check[nx][ny] = i + 1

    # 냄새 줄이기
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                board[i][j][1] -= 1
                if board[i][j][1] == 0:
                    board[i][j] = 0
    
    # 내 냄새 남기기
    for i in range(n):
        for j in range(n):
            if check[i][j]:
                board[i][j] = [check[i][j], k]

    time += 1

print(time)