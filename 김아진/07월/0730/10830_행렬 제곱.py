import sys
input = sys.stdin.readline

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def pow_matrix(n):
    if n == 1:
        return matrix

    half = pow_matrix(n // 2)
    if n % 2 == 0:
        return multi_matrix(half, half)
    else:
        return multi_matrix(multi_matrix(half,half), matrix)


def multi_matrix(m1, m2):
    new_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += m1[i][k] * m2[k][j]
            new_matrix[i][j] = temp % 1000
    
    return new_matrix

answer = pow_matrix(b)
for i in range(n):
    for j in range(n):
        print(answer[i][j] % 1000, end=' ')
    print()