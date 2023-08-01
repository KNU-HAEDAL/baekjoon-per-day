import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

def conquer(i, j):
    num = []
    for k in range(4):
        num.append(matrix[i+dx[k]][j+dy[k]])
    num.sort()

    return num[2]

def divide(n):
    if n == 1:
        return matrix[0][0]

    for i in range(0, n, 2):
        for j in range(0, n, 2):
            matrix[i//2][j//2] = conquer(i, j)
    n //= 2

    return divide(n)

print(divide(n))