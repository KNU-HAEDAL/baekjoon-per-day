import sys
input = sys.stdin.readline

def combination(depth, index):
    if(depth == 6):
        print(*com_num)
        return
    for i in range(index + 1, n):
        com_num.append(num[i])
        combination(depth + 1, i)
        del com_num[com_num.index(num[i])]

while True:      
    line = input().split()
    n = int(line[0])
    if n == 0:
        break

    num = [int(line[i]) for i in range(1,n+1)]
    num.sort()
    com_num = []

    combination(0,-1)
    print()