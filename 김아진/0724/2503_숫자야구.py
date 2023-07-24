import sys
input = sys.stdin.readline

n = int(input())

num_list = []
for i in range(1,1000):
    num = str(i)
    if ('0' not in num) and (len(set(num)) == 3):
        num_list.append(num)
temp = []

for _ in range(n):
    q, s, b = map(int, input().split())
    q_num = str(q)
    for num in num_list:
        strike = 0
        ball = 0

        for j in range(3):
            for k in range(3):
                if q_num[j] == num[k]:
                    if j == k:
                        strike += 1
                    else:
                        ball += 1

        if strike == s and ball == b:
            temp.append(num)
    num_list = temp[ : ]
    temp.clear()

print(len(num_list))