import sys
sys.setrecursionlimit(123458)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
node = [[], [0,0]]

for i in range(N-1):
    kind, number, connection = input().split()
    tree[int(connection)].append(i+2)
    node.append([kind, int(number)])

def dfs(v): 
    result = 0 

    for i in tree[v]:
        result += dfs(i)

    if node[v][0] == 'W':
        result -= node[v][1]
        if result < 0:
            result = 0
    else:
        result += node[v][1]
    return result

print(dfs(1))
