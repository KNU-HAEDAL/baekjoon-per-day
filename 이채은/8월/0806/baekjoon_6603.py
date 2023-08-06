def dfs(depth, idx):
    if depth == 6:
        print(*out)
        return

    for i in range(idx, K):
        out.append(S[i])
        dfs(depth + 1, i + 1)
        out.pop()


while True:
    array = list(map(int, input().split()))
    K = array[0]
    S = array[1:]
    out = []
    dfs(0, 0)
    if K == 0:
        exit()
    print()
