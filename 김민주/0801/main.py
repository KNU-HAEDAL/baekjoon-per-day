# beakjoon 15552 [빠른 A+B]

import sys
T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

# programmers [자릿수 더하기] ; Lelvel 0


def solution(n):
    n = str(n)
    arr = list(n)
    arr = list(map(int, n))
    sum = 0
    for each in arr:
        sum += each
    return sum
