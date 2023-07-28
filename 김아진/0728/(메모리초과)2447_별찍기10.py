import sys
input = sys.stdin.readline

n = int(input())
mem = {}

def print_star(i, j, n):
    if ((i//n) % 3 == 1) and ((j//n) % 3 == 1):
        return ' '
    elif n // 3 == 0:
        return '*'
    else:
        if (i, j, n) in mem:
            return mem[(i,j,n)]
        else:
            result = print_star(i,j,n//3)
            mem[(i,j,n)] = result
            return result

for i in range(n):
    for j in range(n):
        print(print_star(i, j, n), end='')
    print()