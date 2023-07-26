import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*6)

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
direction = [[1, 0], [0, -1], [-1, 0], [0, 1]]
answer = 0

alphabet = [0] * 26

def move_horse(i, j, depth):
    global answer

    if answer  == 26:
        return

    answer = max(depth, answer)
    ch = ord(graph[i][j]) - ord('A')
    alphabet[ch] = 1

    for k in range(4):
        cur_i = i + direction[k][0]
        cur_j = j + direction[k][1]

        if cur_i < 0 or cur_i >= r:
            continue
        if cur_j < 0 or cur_j >= c:
            continue
        
        ch = ord(graph[cur_i][cur_j]) - ord('A')
        if alphabet[ch]:
            continue

        alphabet[ch] = 1
        move_horse(cur_i, cur_j, depth + 1)
        alphabet[ch] = 0


move_horse(0, 0, 1)
        
print(answer)