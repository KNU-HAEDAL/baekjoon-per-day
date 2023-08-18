import sys, copy
input = sys.stdin.readline
from itertools import product
from collections import deque

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
types = [[] for _ in range(6)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
answer = n * m

def seperate_type():
    all_type = list(product(range(2), repeat=4))
    for t in all_type:
        t = ''.join(list(map(str, t)))
        if t.count('1') == 1:
            types[1].append(t)
        if t.count('1') == 2:
            if t == '1010' or t =='0101':
                types[2].append(t)
            else:
                types[3].append(t)
        if t.count('1') == 3:
            types[4].append(t)
        if t.count('1') == 4:
            types[5].append(t)

seperate_type()

cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= office[i][j] <= 5:
            cctv.append((i,j, office[i][j]))

def watch_cctv(x, y, d):
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if 0<=nx<n and 0<=ny<m:
            if office[nx][ny] == 6:
                break
            if office[nx][ny] == 0:
                office[nx][ny] = -1
            x, y = nx, ny
        else:
            break

def dfs(depth):
    global office, answer
    if depth == len(cctv):
        corner = 0
        for j in office:
            corner += j.count(0)
        answer = min(answer, corner)
        return
    x, y, t = cctv[depth]

    board = copy.deepcopy(office)
    for cur_type in types[t]:
        for i in range(4):
            if cur_type[i] == '1':
                watch_cctv(x,y,i)
        dfs(depth+1)
        office = copy.deepcopy(board)

type_index = deque()
dfs(0)
print(answer)