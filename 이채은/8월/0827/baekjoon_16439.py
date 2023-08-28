from itertools import combinations
N, M = map(int, input().split())

likechick = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0

for a,b,c in combinations(range(M), 3):
    sum = 0
    for i in range(N):
        sum += max(likechick[i][a], likechick[i][b], likechick[i][c])
    max_sum = max(max_sum, sum)

print(max_sum)
