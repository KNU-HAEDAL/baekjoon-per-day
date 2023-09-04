import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M, k = map(int, input().split())
parent = [i for i in range(N + 1)]
friend_value = list(map(int, input().split()))

def find(x):
    if parent[x] != x:
        # 루트 노드가 아니면 루트 노드 찾을 때까지 재귀 호출
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        if friend_value[x - 1] <= friend_value[y - 1]:
            parent[y] = x
        else:
            parent[x] = y

for i in range(M):
    v, w = map(int, input().split())
    union(v, w)

check = list()
value = 0
for i in range(1, N + 1):
    if find(i) not in check:
        value += friend_value[parent[i] - 1]
        check.append(parent[i])
        if value > k:
            print('Oh no')
            exit()

print(value)