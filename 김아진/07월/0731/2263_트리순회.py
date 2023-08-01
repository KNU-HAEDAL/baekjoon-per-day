import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
inorder = list(map(int, input().split()))
post = list(map(int, input().split()))
index = [0] * (n+1)

def order(pstart, istart, size):
    if size == 0:
        return

    pend = pstart + size - 1
    node = post[pend]
    print(node, end=' ')
    
    i = index[node]
    s = i - istart
    order(pstart, istart, s)
    pstart += s
    istart += s + 1
    s = size - s - 1
    order(pstart, istart , s)

for i in range(n):
    index[inorder[i]] = i

order(0,0, n)
