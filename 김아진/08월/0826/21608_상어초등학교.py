import sys
input = sys.stdin.readline

n = int(input())
like = [list(map(int, input().split())) for _ in range(n**2)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def select_like_seat(friend, x, y):
    friend = friend[1:]
    count = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if classroom[nx][ny] in friend:
            count += 1
    return count

def select_empty_seat(x, y):
    count = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if classroom[nx][ny] == 0:
            count += 1
    return count

def find_satisfaction(s, x, y):
    friend = like[s-1][1:]
    count = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if classroom[nx][ny] in friend:
            count += 1
    if not count:
        return 0
    else:
        return 10**(count - 1)

classroom = [[0]*n for _ in range(n)]
for like_friend in like:
    max_count = 0
    candidate = []
    for i in range(n):
        for j in range(n):
            if classroom[i][j]:
                continue
            cur_count = select_like_seat(like_friend, i,j)
            if max_count == cur_count:
                candidate.append((i,j))
            elif max_count < cur_count:
                candidate = [(i,j)]
                max_count = cur_count
    
    max_count = 0
    second_candiate = []
    if len(candidate) > 1:
        for i,j in candidate:
            cur_count = select_empty_seat(i,j)
            if max_count == cur_count:
                second_candiate.append([i,j])
            elif max_count < cur_count:
                second_candiate = [[i,j]]
                max_count = cur_count
        second_candiate.sort()
        x, y = second_candiate[0]
    else:
        x, y = candidate[0]

    classroom[x][y] = like_friend[0]

like.sort()
satisfaction = 0
for i in range(n):
    for j in range(n):
        student = classroom[i][j]
        satisfaction += find_satisfaction(student, i, j)
print(satisfaction)