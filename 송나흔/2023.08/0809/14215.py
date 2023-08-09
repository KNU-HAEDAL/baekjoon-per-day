import sys
a, b, c = map(int, sys.stdin.readline().split())
x = []

x.append(a)
x.append(b)
x.append(c)
x.sort()

y = x[0] + x[1]
if x[2] >= y:
    print(y + (y - 1))
else:
    print(y + x[2])