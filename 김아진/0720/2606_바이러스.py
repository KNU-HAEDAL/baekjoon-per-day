import sys
input = sys.stdin.readline

v = int(input())
e = int(input())
graph = [[0]*0 for _ in range(v+1)]
visited = [False] * (v+1)
cnt = 0

def dfs(v):
    global cnt
    visited[v] = True
    cnt += 1

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])

dfs(1)
print(cnt - 1) # 1번 컴퓨터 제외