import sys
input = sys.stdin.readline
number = [0] * 10001

N = int(input())

for _ in range(N):
    number[int(input())] += 1

for i in range(10001):
    if number[i] != 0:
        for j in range(number[i]):
            print(i)
