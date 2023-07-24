import sys
input = sys.stdin.readline

n = int(input())

answer = 0
num = [0]*1000

for _ in range(n):
    q, s, b = map(int, input().split())
    q_num = list(map(int, str(q)))

    for i in range(123, 1000):
        a_num = list(map(int, str(i)))
        strike = 0
        ball = 0

        if a_num[0] == a_num[1] or a_num[0] == a_num[2] or a_num[1] == a_num[2]:
            continue
        if not all([a_num[0], a_num[1], a_num[2]]): # all도 있음
            continue
        
        for j in range(3):
            for k in range(3):
                if a_num[j] == q_num[k]:
                    if j == k:
                        strike += 1
                    else:
                        ball += 1
        
        if strike == s and ball == b:
            num[i] += 1

for i in range(111, 1000):
    if n == num[i]:
        answer += 1

print(answer)