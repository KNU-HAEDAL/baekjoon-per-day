import sys, copy
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
magic = []
for _ in range(m):
    d, s = map(int, input().split())
    magic.append((d-1, s))

def destroy_beads(d, s):
    x, y = n//2, n//2
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for _ in range(s):
        x, y = (x + dx[d]) % n, (y + dy[d]) % n
        board[x][y] = 0

def move_beads():
    x, y = n//2, n//2
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    k = 0

    while True:
        for i in range(4):
            if i % 2 == 0:
                k += 1
            for _ in range(k):
                x, y = x + dx[i], y + dy[i]
                if board[x][y] != 0:
                    beads.append(board[x][y])
                if x == 0 and y == 0:
                    return

def explore_beads():
    global answer, beads
    while True:
        if not beads:
            return
        cur_num, count = beads[0], 1
        temp_beads = []

        for i in range(1, len(beads)):
            if cur_num == beads[i]:
                count += 1
            else:
                if count >= 4:
                    answer += cur_num * count
                else:
                    for j in range(i-1, i-count-1, -1):
                        temp_beads.append(beads[j])
                cur_num, count = beads[i], 1
        if count >= 4:
            answer += cur_num * count
        else:
            for j in range(len(beads)-1, len(beads)-count-1, -1):
                temp_beads.append(beads[j])

        if beads == temp_beads:
            return

        beads = temp_beads

def change_beads():
    global beads
    cur_num, count = beads[0], 1
    temp_beads = []

    for i in range(1, len(beads)):
        if cur_num == beads[i]:
            count += 1
        else:
            temp_beads.extend((count, cur_num))
            cur_num, count = beads[i], 1
    temp_beads.extend((count, cur_num))

    beads = temp_beads

def beads_to_graph():
    global board
    x, y = n//2, n//2
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    k = 0
    index = 0
    temp_board = [[0]*n for _ in range(n)]
    while True:
        for i in range(4):
            if i % 2 == 0:
                k += 1
            for _ in range(k):
                if index == len(beads):
                    board = copy.deepcopy(temp_board)
                    return
                x, y = x + dx[i], y + dy[i]
                temp_board[x][y] = beads[index]
                index += 1
                
                if x == 0 and y == 0:
                    board = copy.deepcopy(temp_board)
                    return

answer = 0
for d, s in magic:
    beads = []
    destroy_beads(d, s)
    move_beads()
    if not beads:
        break
    explore_beads()
    if not beads:
        break
    change_beads()
    beads_to_graph()

print(answer)