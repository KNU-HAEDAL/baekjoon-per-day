import sys
N = int(sys.stdin.readline())

x_list = list()
y_list = list()
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

w = abs(max(x_list) - min(x_list))
h = abs(max(y_list) - min(y_list))
print(w * h)