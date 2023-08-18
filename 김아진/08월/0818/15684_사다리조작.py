import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
laddar = [[False]*(n+1) for _ in range(h+1)]
answer = 4

for _ in range(m):
    r, c = map(int, input().split())
    laddar[r][c] = True

def down_laddar():
    for i in range(1, n):
        c = i
        for r in range(1, h+1):
            if laddar[r][c] == 1:
                c += 1
            elif laddar[r][c-1] == 1:
                c -= 1
        if i != c:
            return False
    return True

def dfs(depth, r, c):
    global answer

    if down_laddar():
        answer = min(answer, depth)
        return

    if depth == 3:
        return

    for i in range(r, h+1):
        if i == r:
            k = c
        else:
            k = 1
        for j in range(k, n):
            if laddar[i][j] == 0 and laddar[i][j-1] == 0 and laddar[i][j+1] == 0:
                laddar[i][j] = 1
                dfs(depth + 1, i, j + 2)
                laddar[i][j] = 0

dfs(0, 1, 1)
if answer == 4:
    answer = -1
print(answer)