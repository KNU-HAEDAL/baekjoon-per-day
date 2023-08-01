import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

t = int(input())
nums = 0

def project(cur):
    global nums

    visited[cur] = True
    team.append(cur)
    node = graph[cur]

    if visited[node] == False:
        project(node)
    else:
        if node in team:
            index = team.index(node)
            nums += len(team[index:])
            return
while t:
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [True] + [False]*n
    nums = 0
    
    for i in range(1, n+1):
        team = []
        if visited[i] == False:
            project(i)
    
    print(n - nums)
    t -= 1