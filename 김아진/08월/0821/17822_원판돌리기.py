import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(n)]

for _ in range(t):
    x, d, k = map(int, input().split())
    # 원판 돌리기
    i = x
    while i <= n:
        for _ in range(k):
            cur_plate = []
            if d == 0:
                cur_plate.append(plate[i-1][m-1])
                cur_plate.extend(plate[i-1][:m-1])
            else:
                cur_plate.extend(plate[i-1][1:m])
                cur_plate.append(plate[i-1][0])
            plate[i-1] = cur_plate
        i += x
    
    # 인접한 거 지우기
    remove_index = set()
    for i in range(n):
        for j in range(m):
            if plate[i][j] == 0:
                continue
            if plate[i][j] == plate[i][j-1]:
                remove_index.add((i,j))
                remove_index.add((i,j-1))
    for j in range(m):
        for i in range(1,n):
            if plate[i][j] == 0:
                continue
            if plate[i][j] == plate[i-1][j]:
                remove_index.add((i,j))
                remove_index.add((i-1, j))

    if len(remove_index) > 0:
        for i, j in remove_index:
            plate[i][j] = 0
    else:
        average = 0
        cnt = 0
        for i in range(n):
            for j in range(m):
                if plate[i][j] != 0:
                    average += plate[i][j]
                    cnt += 1
        if average != 0:
            average /= cnt
            for i in range(n):
                for j in range(m):
                    if plate[i][j] == 0:
                        continue
                    if plate[i][j] > average:
                        plate[i][j] -= 1
                    elif plate[i][j] < average:
                        plate[i][j] += 1
    
# 합 구하기
answer = 0
for i in plate:
    answer += sum(i)
print(answer)