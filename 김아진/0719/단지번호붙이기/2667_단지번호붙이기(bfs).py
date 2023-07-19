import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
graph = [[0]*0 for _ in range(n)]
visited = [[False]*n for _ in range(n)]
direction = [[1,0], [0,1], [-1,0], [0,-1]]
queue = []
block = []

def bfs(i, j):
    home = 1
    queue = deque([(i,j)])
    visited[i][j] = True

    while queue:
        v = queue.popleft()

        for k in range(4):
            cur_i = int(v[0]) + direction[k][0]
            cur_j = int(v[1]) + direction[k][1]

            if(cur_i < 0 or cur_i >= n):
                continue
            if(cur_j < 0 or cur_j >= n):
                continue

            if graph[cur_i][cur_j] == 1 and not visited[cur_i][cur_j]:
                home += 1
                queue.append((cur_i, cur_j))
                visited[cur_i][cur_j] = True

    block.append(home)

for i in range(n):
    temp = list(input())
    for j in range(n):
        graph[i].append(int(temp[j]))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i,j)

print(len(block))
block.sort()
print(*block, sep='\n')