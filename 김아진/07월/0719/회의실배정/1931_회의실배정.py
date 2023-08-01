import sys
input = sys.stdin.readline

n = int(input())
meeting = []
cnt = 1

for i in range(n):
    tmp1, tmp2 = map(int, input().split())
    meeting.append((tmp1, tmp2))

meeting.sort(key=lambda x: (x[1], x[0]))

finish = meeting[0][1]
for i in range(1, n):
    if finish <= meeting[i][0]:
        cnt += 1
        finish = meeting[i][1]

print(cnt)
