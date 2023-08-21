import sys
input = sys.stdin.readline

n = int(input())
A = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    A[i+1] = [0] + list(map(int, input().split()))

def divide_boundary(x, y, d1, d2):
    election = [0]*5
    temp = [[0]*(n+1) for _ in range(n+1)]
    
    # 경계선 설정하기
    for i in range(1, d1+1):
        temp[x+i][y-i] = 5
    for i in range(1, d2+1):
        temp[x+i][y+i] = 5
    for i in range(1, d2+1):
        temp[x+d1+i][y-d1+i] = 5
    for i in range(1, d1+1):
        temp[x+d2+i][y+d2-i] = 5
    temp[x][y] = 5

    # 1구역
    for i in range(1, x+d1):
        for j in range(1, y+1):
            if temp[i][j] == 5:
                break
            election[0] += A[i][j]
            temp[i][j] = 1
    # 2구역
    for i in range(1, x+d2+1):
        for j in range(n, y, -1):
            if temp[i][j] == 5:
                break
            election[1] += A[i][j]
            temp[i][j] = 2
    # 3구역
    for i in range(x+d1, n+1):
        for j in range(1, y-d1+d2):
            if temp[i][j] == 5:
                break
            election[2] += A[i][j]
            temp[i][j] = 3
    # 4구역
    for i in range(x+d2+1, n+1):
        for j in range(n, y-d1+d2-1, -1):
            if temp[i][j] == 5:
                break
            election[3] += A[i][j]
            temp[i][j] = 4
    # 5구역
    for i in range(1,n+1):
        for j in range(1,n+1):
            if temp[i][j] == 0 or temp[i][j] == 5:
                election[4] += A[i][j]
                temp[i][j] = 5

    diff = max(election) - min(election)
    return diff

answer = sys.maxsize
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n-1):
            for d2 in range(1, n-1):
                if x + d1 + d2 > n:
                    continue
                if y - d1 < 1:
                    continue
                if y + d2 > n:
                    continue
                answer = min(answer, divide_boundary(x,y,d1,d2))
print(answer)