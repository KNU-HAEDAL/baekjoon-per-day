import sys

num = int(sys.stdin.readline())
sum = 1
for i in range(num):
    tempNum = int(sys.stdin.readline())
    sum+=tempNum

print(sum-num)
