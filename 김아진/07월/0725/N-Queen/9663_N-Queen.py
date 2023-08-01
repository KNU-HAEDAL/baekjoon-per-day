import sys, math
input = sys.stdin.readline

n = int(input())
dia1 = [0] * (2*n + 1)
dia2 = [0] * (2*n + 1)
col = [0]*n
answer = 0

def n_queen(depth):
    global answer
    if(depth == n):
        answer += 1
        return

    i = depth
    for j in range(n):
        if col[j] + dia1[i+j] + dia2[n-(i-j)]:
            continue
        col[j] = dia1[i+j] = dia2[n-(i-j)] = 1
        n_queen(depth+1)
        col[j] = dia1[i+j] = dia2[n-(i-j)] = 0

n_queen(0)
print(answer)