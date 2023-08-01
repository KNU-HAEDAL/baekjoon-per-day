import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
n_graph = [list(input().rstrip()) for _ in range(n)]
w_graph = copy.deepcopy(n_graph)
direction = [[1,0],[0,-1],[-1,0],[0,1]]
n_color = 0
w_color = 0

def slice_area(r, c, color, graph):
    graph[r][c] = 0
    for i in range(4):
        cur_i = r + direction[i][0]
        cur_j = c + direction[i][1]

        if cur_i < 0 or cur_i >= n:
            continue
        if cur_j < 0 or cur_j >= n:
            continue

        if graph[cur_i][cur_j] == color:
            graph[cur_i][cur_j] = 0
            slice_area(cur_i, cur_j, color, graph)

for i in range(n):
    for j in range(n):
        if w_graph[i][j] == 'G':
            w_graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if n_graph[i][j]:
            n_color += 1
            slice_area(i, j, n_graph[i][j], n_graph)

        if w_graph[i][j]:
            w_color += 1
            slice_area(i, j, w_graph[i][j], w_graph)

print(n_color, w_color)