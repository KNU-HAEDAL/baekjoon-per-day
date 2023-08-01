import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

from collections import deque

t = int(input())
dir = [[1, 0], [0, -1], [-1, 0], [0, 1]]

def put_worm(r,c):
    graph[r][c] = 2

    for k in range(4):
        cur_i = r + dir[k][0]
        cur_j = c + dir[k][1]

        if cur_i < 0 or cur_i > m - 1:
            continue
        if cur_j < 0 or cur_j > n - 1:
            continue
        
        if graph[cur_i][cur_j] != 1:
            continue

        graph[cur_i][cur_j] = 2
        put_worm(cur_i, cur_j)

for _ in range(t):
    answer = 0
    m, n, k = map(int, input().split())
    
    graph = [[0] * n for _ in range(m)]
    for i in range(k):
        r, c = map(int, input().split())
        graph[r][c] = 1

    for i in range(m):
        for j in range(n):
            if graph[i][j] != 1: 
                continue

            answer += 1
            put_worm(i,j)

    print(answer)