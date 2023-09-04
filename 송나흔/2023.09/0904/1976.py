import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
M = int(input())
parent = [i for i in range(N + 1)]
check = [list(map(int, input().split())) for _ in range(N)]

def find(x):
    if parent[x] != x:
        # 루트 노드가 아니면 루트 노드 찾을 때까지 재귀 호출
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(N):
    for j in range(N):
        if check[i][j] == 1:
            union(i, j)

ans = list(map(int, input().split()))
for i in range(1, M):
    if parent[ans[i] - 1] != parent[ans[0] - 1]:
        print('NO')
        exit()

print('YES')