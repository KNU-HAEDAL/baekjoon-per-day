import sys, copy
input = sys.stdin.readline

dice = list(map(int, input().split()))
horse = [0]*4

board = [
    [1],[2],[3],[4],[5],
    [6,21],[7],[8],[9],[10],
    [11,25],[12],[13],[14],[15],
    [16,27],[17],[18],[19],[20],
    [32],[22],[23],[24],[30],
    [26],[24],[28],[29],[24],
    [31],[20],[32]
]
score = [
    0, 2, 4, 6, 8,
    10, 12, 14, 16, 18,
    20, 22, 24, 26, 28,
    30, 32, 34, 36, 38,
    40, 13, 16, 19, 25,
    22, 24, 28, 27, 26,
    30, 35, 0
]

answer = 0
def play_game(n, s):
    global answer
    if n == 10:
        answer = max(answer, s)
        return
    
    # 말 4개 움직이기
    for i in range(4):
        x = horse[i]

        # 시작 점이 파란색이라면
        if len(board[x]) == 2:
            x = board[x][1]
        else:
            x = board[x][0]
        
        # 주사위 수 - 1 만큼 움직이기
        for _ in range(1, dice[n]):
            x = board[x][0]

        # 종료하거나 중복 안되면
        if x == 32 or (x<32 and x not in horse):
            temp = horse[i]
            horse[i] = x
            play_game(n+1, s + score[x])
            horse[i] = temp

play_game(0,0)
print(answer)