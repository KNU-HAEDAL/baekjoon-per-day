import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

def zip_video(x, y, n):
    if n == 1:
        return graph[x][y]

    n //= 2
    v1 = str(zip_video(x, y, n))
    v2 = str(zip_video(x, y+n, n))
    v3 = str(zip_video(x+n, y, n))
    v4 = str(zip_video(x+n, y+n, n))
    
    if v1 == v2 == v3 == v4 and len(v1) == 1:
        return v1
    else:
        return f"({v1}{v2}{v3}{v4})"        

print(zip_video(0,0,n))
