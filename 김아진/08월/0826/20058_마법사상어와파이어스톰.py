import sys, copy
input = sys.stdin.readline
from collections import deque

n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**n)]
L = list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ice_size, max_ice = 0, 0

def storm(x, y, cur_L):
    temp = []
    for i in range(2**cur_L):
        temp.append(board[x+i][y:y+2**cur_L])
    temp = list(map(list, zip(*temp[::-1])))
    
    for i in range(2**cur_L):
        for j in range(2**cur_L):
            board[x+i][y+j] = temp[i][j]

def check_ice(x, y, ice_count):
    global ice_size, max_ice

    ice_size += board[x][y]
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= 2**n or ny >= 2**n:
                continue
            if visited[nx][ny] or board[nx][ny] <= 0:
                continue

            queue.append((nx,ny))
            ice_size += board[nx][ny]
            visited[nx][ny] = True
            ice_count += 1

    max_ice = max(max_ice, ice_count)

for cur_L in L:
    
    # L만큼 회전하기
    time = (2**n)//(2**cur_L)
    for i in range(time):
        for j in range(time):
            storm(i*(2**cur_L), j*(2**cur_L), cur_L)

    # 얼음 녹이기
    new_board = [[0]*(2**n) for _ in range(2**n)]
    for x in range(2**n):
        for y in range(2**n):
            ice_count = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= 2**n or ny >= 2**n:
                    continue
                if board[nx][ny] <= 0:
                    continue
                ice_count += 1
            if ice_count < 3:
                new_board[x][y] = board[x][y] - 1
            else:
                new_board[x][y] = board[x][y]
    board = copy.deepcopy(new_board)

# 얼음 확인하기
visited = [[False]*(2**n) for _ in range(2**n)]
for i in range(2**n):
    for j in range(2**n):
        if not visited[i][j] and board[i][j] > 0:
           check_ice(i,j,1)

print(ice_size)
print(max_ice)