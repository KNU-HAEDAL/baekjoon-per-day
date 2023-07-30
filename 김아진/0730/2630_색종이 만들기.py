import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

def cut_paper(x,y, n):
    if n == 0:
        return
    
    global white, blue
    color = paper[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                n //= 2
                cut_paper(x, y, n)
                cut_paper(x+n, y, n)
                cut_paper(x, y+n, n)
                cut_paper(x+n, y+n, n)
                return

    if color == 1:
        blue += 1
    else:
        white += 1

cut_paper(0,0, n)
print(white)
print(blue)