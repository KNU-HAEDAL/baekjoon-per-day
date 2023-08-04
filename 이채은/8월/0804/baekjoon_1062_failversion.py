import sys

input = sys.stdin.readline
N, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(input().strip())

origins = ['a', 'n', 't', 'i', 'c']
anothers = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
              'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']

def selecting(n, start):
    global result
    if n == 0:
        result = max(result, checking())
        return
    for i in range(start, len(anothers)):
        origins.append(anothers[i])
        selecting(n-1, i+1)
        origins.pop()

def checking():
    result = 0
    for words in arr:
        isRead = True
        for i in range(4, len(words)-4):
            if words[i] not in origins:
                isRead = False
                break
        if isRead:
            result += 1
    return result

result = 0
if K < 5:
    print(result)
else:
    selecting(K-5, 0)
    print(result)
