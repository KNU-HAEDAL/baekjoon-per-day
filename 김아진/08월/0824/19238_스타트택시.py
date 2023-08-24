import sys
input = sys.stdin.readline
from collections import deque

n, m, fuel = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
tx, ty = list(map(int, input().split()))
guest = [list(map(int, input().split())) for _ in range(m)]

tx, ty = tx - 1, ty - 1
for i in range(m):
    x, y, nx, ny = guest[i]
    guest[i] = [x-1, y-1, nx-1, ny-1]
guest.sort()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def choose_guest(x, y, fuel):
    queue = deque([(x,y)])
    visited = [[0]*n for _ in range(n)]
    min_distance = sys.maxsize
    candiate = []
    while queue:
        x, y = queue.popleft()
        # 연료 떨어지면 종료
        if fuel < visited[x][y]:
            return -1, -1
        # 최단 거리보다 더 가면 bfs 그만돌기
        if visited[x][y] > min_distance:
            break
        # 현재 위치에 손님 있으면 후보로 넣기
        if people[x][y] > -1:
            min_distance = visited[x][y]
            candiate.append([x,y])
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] or graph[nx][ny] == 1:
                continue
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))
    
    if candiate:
        candiate.sort()
        # 상단 좌측에 위치한 손님 우선 선택하기
        x, y = candiate[0]
        return people[x][y], visited[x][y]

    # 태울 손님 없으면 에러 리턴
    return -1, -1

def go_destination(x, y, fuel, gx, gy):
    queue = deque([(x,y)])
    visited = [[0]*n for _ in range(n)]
    while queue:
        x, y = queue.popleft()
        # 연료 떨어지면 종료
        if fuel < visited[x][y]:
            return -1

        # 목적지 도착하면 종료
        if gx == x and gy == y:
            return visited[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] or graph[nx][ny] == 1:
                continue
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))
    
    # 목적지 도착 못하면 에러 리턴
    return -1

while True:
    # 더이상 태울 손님 없으면 종료
    if not guest:
        print(fuel)
        break
    
    # 손님 위치 기록하기
    people = [[-1]*n for _ in range(n)]
    for i, cur_guest in enumerate(guest):
        x, y, _, _ = cur_guest
        people[x][y] = i

    # bfs돌면서 손님 선택하기
    num, spent_fuel = choose_guest(tx, ty, fuel)
    if num == -1:
        print(-1)
        break
    
    # 출발지로 가기
    fuel -= spent_fuel
    tx, ty = guest[num][0], guest[num][1]

    # 목적지로 가기
    spent_fuel = go_destination(tx, ty, fuel, guest[num][2], guest[num][3])
    if spent_fuel == -1:
        print(-1)
        break
    
    # 연료 충전하기
    fuel += spent_fuel
    tx, ty = guest[num][2], guest[num][3]

    # 손님 삭제
    guest.pop(num)