import sys
N = int(sys.stdin.readline())
row = 2

for i in range(N):
    row += 2 ** i

print(row ** 2)