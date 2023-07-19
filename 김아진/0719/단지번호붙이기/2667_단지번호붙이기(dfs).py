import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
block = []
home = 0

def dfs(i, j):
    global home
    graph[i][j] = 0 # 0이면 visited
    
    for k in range(4):
        cur_i = i + direction[k][0]
        cur_j = j + direction[k][1]

        if cur_i < 0 or cur_i >= n:
            continue
        if cur_j < 0 or cur_j >= n:
            continue

        if graph[cur_i][cur_j] == 1:
            home += 1
            dfs(cur_i, cur_j)
    

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home = 1
            dfs(i, j)
            block.append(home)

print(len(block))
block.sort()
print(*block, sep="\n")