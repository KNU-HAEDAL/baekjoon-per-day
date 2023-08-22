import sys
input = sys.stdin.readline
green = [[0]*4 for _ in range(6)]
blue = [[0]*4 for _ in range(6)]
answer = 0
def down_block(graph, t, y):
    global answer
    
    # 다음 위치 구하기
    x = 0
    while True:
        if x == 5:
            break
        if graph[x+1][y]:
            break
        if t == 2 and graph[x+1][y+1]:
            break
        x += 1

    # 블럭 놓기
    graph[x][y] = 1
    if t == 2:
        graph[x][y+1] = 1
    if t == 3:
        graph[x-1][y] = 1

    # 한 줄씩 팡!
    remove_row = []
    for i in range(5,-1,-1):
        if sum(graph[i]) == 4:
            answer += 1
            remove_row.append(i)
    
    for i in remove_row:
        graph.pop(i)
        
    for _ in range(len(remove_row)):
        graph.insert(0, [0]*4)

    # 특별한 칸 처리하기
    while True:
        if sum(graph[1]) != 0:
            graph.pop()
            graph.insert(0, [0]*4)
        else:
            break

n = int(input())
for _ in range(n):
    t, x, y = map(int, input().split())
    
    down_block(green, t, y)
    
    if t == 2:
        t = 3
    elif t == 3:
        t = 2
        x += 1
    
    down_block(blue, t, 3-x)


print(answer)
count = 0
for i in range(6):
    count += sum(green[i])
    count += sum(blue[i])
print(count)