import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

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

for i in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')