import sys
from itertools import combinations

n = int(sys.stdin.readline())
answer = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        num = sorted(list(j), reverse=True)
        answer.append(int("".join(map(str, num))))

answer.sort() 
print(answer[n] if len(answer) > n else -1) 
