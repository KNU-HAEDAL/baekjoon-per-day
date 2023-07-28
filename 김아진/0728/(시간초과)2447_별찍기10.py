import sys
input = sys.stdin.readline

n = int(input())

def print_star(i, j, n):
    if ((i//n) % 3 == 1) and ((j//n) % 3 == 1):
        print(' ', end='')
    elif n // 3 == 0:
        print('*', end='')
    else:
        print_star(i,j,n//3)


for i in range(n):
    for j in range(n):
        print_star(i, j, n)
    print()