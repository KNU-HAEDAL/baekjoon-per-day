import sys
N, B = map(int, sys.stdin.readline().split())

Ans = list()
i = 0
while N >= B:
    temp = N % B
    if temp > 9:
        Ans.append(chr(temp + 55))
    else:
        Ans.append(temp)
    N = N // B
    i += 1

if N > 9:
    Ans.append(chr(N + 55))
else:
    Ans.append(N)
Ans = list(reversed(Ans))
length = len(Ans)

for i in range(length):
    print(Ans[i], end = '')