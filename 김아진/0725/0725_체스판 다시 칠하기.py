import sys
input = sys.stdin.readline
wcolor = ['W', 'B']
bcolor = ['B', 'W']
answer = sys.maxsize

def check_board(row, col, color):
    cnt = 0
    for i in range(8):
        for j in range(8):
            digit = (i + j) % 2
            if not digit:
                if board[row + i][col + j] == color[digit]:
                    cnt += 1  
            else:
                if board[row + i][col + j] == color[digit]:
                    cnt += 1
    return min(cnt, answer)


r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

for i in range(r - 8 + 1):
    for j in range(c - 8 + 1):
        answer = min(check_board(i,j,wcolor), check_board(i,j, bcolor))

print(answer)