import sys
input = sys.stdin.readline

from heapq import heappush, heappop

n = int(input())
lecture = []
room = []


for i in range(n):
    tmp1, tmp2 = map(int, input().split())
    lecture.append((tmp1, tmp2))

lecture.sort()
heappush(room, lecture[0][1])  # 0번째 강의의 시작 시간

for i in range(n-1):
    if room[0] <= lecture[i+1][0]:
        heappop(room)
    heappush(room, lecture[i+1][1])

print(len(room))
