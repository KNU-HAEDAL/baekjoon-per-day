import sys
input = sys.stdin.readline

gears = [list(map(int, input().rstrip())) for _ in range(4)]
k = int(input())

def select_direction(n):
    if n+1 < 4 and visited[n+1] == 0 and gears[n+1][6] != gears[n][2]:
        visited[n+1] = -visited[n]
        select_direction(n+1)
    if n-1 >= 0 and visited[n-1] == 0 and gears[n-1][2] != gears[n][6]:
        visited[n-1] = -visited[n]
        select_direction(n-1)

def rotate_gear(gear, d):
    if d == 1:
        gear = [gear[7]] + gear[:-1]
    if d == -1:
        gear = gear[1:] + [gear[0]]
    return gear

for _ in range(k):
    n, d = map(int, input().split())
    visited = [0] * 4
    visited[n-1] = d
    
    select_direction(n-1)
    for i in range(4):
        gears[i] = rotate_gear(gears[i], visited[i])

answer = 0
for i in range(4):
    if gears[i][0] == 1:
        answer += 2**i
print(answer)