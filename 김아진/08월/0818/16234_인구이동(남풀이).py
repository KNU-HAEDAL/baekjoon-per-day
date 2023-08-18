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

def move_people(country):
    # 공유 인구 수 구하기
    people = 0
    for x,y in country:
        people += land[x][y]
    
    # 인구 이동하기
    people //= len(country)
    for x,y in country:
        land[x][y] = people

day = 0
while True:
    visited = [[False]*n for _ in range(n)]
    unions = []
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                # 국경선 공유하기
                visited[i][j] = True
                country = bfs(i,j)
                
                # 이동할 연합 추가
                if len(country) > 1:
                    unions.append(country)
    
    # 연합 없으면 종료
    if not unions:
        break

    # 연합 하나씩 보면서 사람들 이동시키기
    day += 1
    for union in unions:
        move_people(union)

print(day)