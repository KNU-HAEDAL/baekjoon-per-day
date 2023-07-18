from collections import deque

import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0] * 0 for _ in range(n+1)]

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])

dfs_visit = [False] * (n+1)
bfs_visit = [False] * (n+1)


def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)


def bfs(start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(v, dfs_visit)
print()
bfs(v, bfs_visit)
