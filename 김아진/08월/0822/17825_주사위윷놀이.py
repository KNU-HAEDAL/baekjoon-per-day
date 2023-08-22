import sys, copy
input = sys.stdin.readline

dice = list(map(int, input().split()))
horse = [[0]*2 for _ in range(4)]
board = [
    [i*2 for i in range(21)],
    [10, 13, 16, 19, 25, 30, 35, 40],
    [20, 22, 24, 25, 30, 35, 40],
    [30, 28, 26, 26, 25, 30, 35, 40]
]

answer = 0
def play_game(n, score, horse):
    print(horse)
    global answer
    if n == 10:
        answer = max(answer, score)
        return
    
    # 4개의 말 완전탐색
    for i in range(4):
        # 종료된 말
        if horse[i][0] == -1:
            continue
        cur_horse = copy.deepcopy(horse)

        # 주사위 굴려서 현재 말 이동하기
        cur_horse[i][0] += dice[n]

        # 파란색 칸인지 확인하기
        if cur_horse[i][1] == 0:
            if cur_horse[i][0] == 5:
                cur_horse[i] = [0, 1]
            elif cur_horse[i][0] == 10:
                cur_horse[i] = [0, 2]
            elif cur_horse[i][0] == 15:
                cur_horse[i] = [0, 3]
        
        # 종료되는 지 확인하기
        if cur_horse[i][0] >= len(board[cur_horse[i][1]]):
            cur_horse[i][0] = -1
            play_game(n+1, score, cur_horse)
            continue

        # 이동한 위치에 말 있는지 확인하기
        check = False
        num = board[cur_horse[i][1]][cur_horse[i][0]]
        for j in range(4):
            if i == j:
                continue
            if cur_horse[j][0] == -1:
                continue
            if num != board[cur_horse[j][1]][cur_horse[j][0]]:
                continue
            if num in [16, 22, 24, 26, 28, 30]:
                if cur_horse[i] == cur_horse[j]:
                    check = True
                    break
            else:
                    check = True
                    break
        if check:
            continue
        # 다음 주사위 굴리기
        play_game(n+1, score + num, cur_horse)

play_game(0,0,horse)
print(answer)