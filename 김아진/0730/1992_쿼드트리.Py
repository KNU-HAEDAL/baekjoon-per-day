import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

def zip_video(x, y, n):
    digit = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if digit != graph[i][j]:
                n //= 2
                print('(',end='')
                zip_video(x, y, n)
                zip_video(x, y+n, n)
                zip_video(x+n, y, n)
                zip_video(x+n, y+n, n)
                print(')',end='')
                return
    print(digit,end='')

zip_video(0,0,n)