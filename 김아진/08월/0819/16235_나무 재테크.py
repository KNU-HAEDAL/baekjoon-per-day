import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
ground = [[5]*n for _ in range(n)]
trees = [[list() for _ in range(n)] for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

def spring_summer():
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                trees[i][j].sort()
                live, dead = [], 0
                for tree in trees[i][j]:
                    if tree <= ground[i][j]:
                        live.append(tree + 1)
                        ground[i][j] -= tree
                    else:
                        dead += tree // 2
                trees[i][j] = live
                ground[i][j] += dead

def fall():
    for i in range(n):
        for j in range(n):
            if len(trees[i][j]) == 0:
                continue
            for tree in trees[i][j]:
                if tree % 5 == 0:
                    for k in range(8):
                        nx, ny = i + dx[k], j + dy[k]
                        if 0<=nx<n and 0<=ny<n:
                            trees[nx][ny].append(1)

def winter():
    for i in range(n):
        for j in range(n):
            ground[i][j] += A[i][j]

for _ in range(k):
    spring_summer()
    fall()
    winter()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])
print(answer)