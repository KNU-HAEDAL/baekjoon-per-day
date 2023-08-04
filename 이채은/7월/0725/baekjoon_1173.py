import sys

if __name__ == '__main__':
    N, m, M, T, R = map(int, sys.stdin.readline().split())
    minute, ex_minute = 0, 0
    Pulse = m

    while ex_minute < N:
        if m + T > M:
            break
        if Pulse + T <= M:
            Pulse += T
            ex_minute += 1
        else:
            Pulse = max(Pulse - R, m)
        minute += 1
      
    print(minute if ex_minute == N else -1)
