import sys
input = sys.stdin.readline

n, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

def make_slide(path):
    for i in range(1, n):
        # 높이 차이 1이상이면 false
        if abs(path[i] - path[i-1]) > 1:
            return False
        
        # 3 2 2 2
        if path[i] < path[i-1]:
            # 오른쪽으로 L만큼 보면서
            for j in range(L):
                # 범위, 숫자, 경사로 여부 체크
                if i + j >= n or path[i] != path[i + j] or slide[i + j]:
                    return False
                # 경사로 세우기
                slide[i + j] = True

        # 2 2 2 3
        if path[i] > path[i-1]:
            # 왼쪽으로 L만큼 보면서
            for j in range(1, L+1):
                if i - j < 0 or path[i - 1] != path[i - j] or slide[i - j]:
                    return False
                slide[i - j] = True

    # 경사로 세우는 데 문제 없으면 true
    return True

# row 방향으로 한 줄씩 체크하기
for i in range(n):
    slide = [False] * n
    if make_slide(graph[i]):
        cnt += 1

# 그래프 90도 회전
vertical_graph = list(zip(*graph))

# col 방향으로 한 줄씩 체크하기
for i in range(n):
    slide = [False] * n
    if make_slide(vertical_graph[i]):
        cnt += 1

print(cnt)