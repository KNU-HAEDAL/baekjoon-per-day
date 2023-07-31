import sys
input = sys.stdin.readline

n = int(input())
chicken = list(map(int, input().split()))
k = int(input())

m = n // k
s = 0
while s < n:
    print(*sorted(chicken[s:s+m]), end=' ')
    s += m