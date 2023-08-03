import sys
input = sys.stdin.readline
from collections import deque

command = ['D', 'S', 'L', 'R']

def DSLR(A, B):
    queue = deque([(A,'')])
    visited[A] = True
    while queue:
        A, cmd = queue.popleft()
        if A == B:
            return cmd
            
        calcul = [2*A, A-1, A*10+(A//1000), (A%10)*1000+A//10]
        for i in range(4):
            nextA = calcul[i] % 10000
            if not visited[nextA]:
                visited[nextA] = True 
                queue.append((nextA, cmd + command[i]))

t = int(input())
while t:
    A, B = map(int, input().split())
    visited = ['' for _ in range(10000)]

    print(DSLR(A, B))
    
    t -= 1