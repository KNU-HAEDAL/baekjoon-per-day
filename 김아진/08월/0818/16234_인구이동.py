import sys
input = sys.stdin.readline
from collections import deque

n, L, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    queue = deque([(x,y)])
    country = []
    country.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if L <= abs(land[x][y] - land[nx][ny]) <= R:
                visited[nx][ny] = True
                country.append((nx, ny))
                queue.append((nx, ny))
    return country

day = 0
while True:
    visited = [[False]*n for _ in range(n)]
    check = False
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                # 국경선 공유하기
                visited[i][j] = True
                country = bfs(i,j)

                if len(country) > 1:
                    check = True
                    # 공유 인구 수 구하기
                    people = 0
                    for x,y in country:
                        people += land[x][y]
                    
                    # 인구 이동하기
                    people //= len(country)
                    for x,y in country:
                        land[x][y] = people

    # 이동할 사람 없으면 그만하기
    if not check:
        break
    
    # 하루가 지납니다..
    day += 1

print(day)