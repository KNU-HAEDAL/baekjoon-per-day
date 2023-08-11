import sys
input = sys.stdin.readline
from math import ceil

n = int(input())
test = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = 0

for i in range(n):
    test[i] -= b
    cnt += 1
    if(test[i] > 0):
        cnt += ceil(test[i] / c)

print(cnt)