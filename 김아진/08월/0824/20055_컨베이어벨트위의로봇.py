import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0] * n)

step = 1
while True:
    # 회전하기
    belt.rotate(1)
    robot.rotate(1)

    # 내리는 위치에서 로봇 내리기
    robot[-1] = 0
    
    # 로봇 움직이기
    if sum(robot):
        for i in range(n-2, -1, -1):
            if robot[i] and not robot[i+1]:
                if belt[i+1]:
                    robot[i], robot[i+1] = 0, 1
                    belt[i+1] -= 1

    # 올리는 위치에서 로봇 올리기
    if belt[0]:
        robot[0] = 1
        belt[0] -= 1
    
    # 내리는 위치에서 로봇 내리기
    robot[-1] = 0
    
    # 내구도 체크
    if belt.count(0) >= k:
        print(step)
        break

    step += 1