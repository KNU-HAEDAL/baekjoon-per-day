import sys

N, M = map(int, sys.stdin.readline().split())
rect = [list(map(int ,sys.stdin.readline().strip())) for _ in range(N)]
answer = []

for i in range(N):
    for j in range(M):
        target = rect[i][j] 
        for k in range(j, M):
            if rect[i][k] == target and i + k - j < N and k < M:
              if rect[i + k - j][j] == target and rect[i + k - j][k] == target:
                  answer.append((k - j + 1) ** 2)

print(max(answer))
