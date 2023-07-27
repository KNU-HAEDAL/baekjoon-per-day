N = int(input())
numss = [0] * 10
num = 1

def first_process(N):
    while N % 10 != 9:
        for i in str(N):
            numss[int(i)] += num
        N -= 1
    return N

while N > 0:
    N = first_process(N)
    if N < 10:
        for i in range(N + 1):
            numss[i] += num
    else:
        for i in range(10):
            numss[i] += (N // 10 + 1) * num
    numss[0] -= num
    num *= 10
    N //= 10

for i in range(0, 10):
    print(numss[i], end=' ')
