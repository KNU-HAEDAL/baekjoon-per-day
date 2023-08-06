import sys
T = int(sys.stdin.readline())

for i in range(T):
    C = int(sys.stdin.readline())
    ans = [0 for i in range(4)]
    while True:
        if C >= 25:
            ans[0] = C // 25
            C = C % 25
        elif C >= 10:
            ans[1] = C // 10
            C = C % 10
        elif C >= 5:
            ans[2] = C // 5
            C = C % 5
        else:
            ans[3] = C
            break
    for j in range(4):
        print(ans[j], end = " ")
    print()
