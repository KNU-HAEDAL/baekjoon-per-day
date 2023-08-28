import sys, copy
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cloud_direction = []
for _ in range(m):
    d, s = map(int, input().split())
    cloud_direction.append((d-1, s))

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 비바라기 시전하기
cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

# 구름 이동하기
for cur_d in cloud_direction:
    # d방향으로 s칸 이동
    d, s = cur_d
    for index, cur_cloud in enumerate(cloud):
        x, y = cur_cloud
        nx, ny = (x + dx[d]*s) % n, (y + dy[d]*s) % n
        cloud[index] = (nx, ny)
        
        # 비바구니 1 증가
        board[nx][ny] += 1
    
    # 물 복사 버그
    for x, y in cloud:
        for i in range(1, 8, 2):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[nx][ny] > 0:
                board[x][y] += 1

    # 새로운 구름 생기기
    new_cloud = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and (i,j) not in cloud:
                new_cloud.append((i,j))
                board[i][j] -= 2

    # 기존 구름 사라지기
    cloud = new_cloud
    
water = 0
for i in range(n):
    for j in range(n):
        water += board[i][j]
print(water)