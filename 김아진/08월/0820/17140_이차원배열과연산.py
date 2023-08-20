import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

def sort_array(R, C):
    size = 0
    for i in range(R):
        dic = {}
        for j in range(C):
            if A[i][j] in dic:
                dic[A[i][j]] += 1
            else:
                dic[A[i][j]] = 1
        
        # 0 제거
        if 0 in dic:
            del dic[0]
        # 등장횟수, 수 순서로 정렬
        dic = sorted(dic.items(), key=lambda x:(x[1],x[0]))
        
        A[i] = []
        for num, times in dic:
            A[i].append(num)
            A[i].append(times)
        size = max(len(dic)*2, size)

    # 0 으로 남은 거 채우기
    for line in A:
        remain = 0
        if len(line) < size:
            remain = size - len(line)
        if size < 3:
            remain = 3 - len(line)
        for i in range(remain):
            line.append(0)

    # 가로 크기
    return size

t = 0
R, C = 3, 3
while True:
    if t > 100:
        print(-1)
        break

    if r <= R and c <= C and A[r-1][c-1] == k:
        print(t)
        break

    if R >= C:
        C = sort_array(R, C)
    else:
        A = list(map(list, zip(*A)))
        R = sort_array(C, R)
        A = list(map(list, zip(*A)))

    t += 1