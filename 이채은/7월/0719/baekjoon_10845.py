from sys import stdin

N = int(stdin.readline())
que = []
for i in range(N) :
    input = stdin.readline().split()

    if input[0] == 'push' : que.append(input[1])

    elif input[0] == 'pop' : 
        if que : print(que.pop(0))
        else : print(-1)

    elif input[0] == 'size' : print(len(que))

    elif input[0] == 'empty' :
        if len(que) == 0 : print(1)
        else : print(0)
            
    elif input[0] == 'front' :
        if len(que) == 0 : print(-1)
        else : print(que[0])
    
    elif input[0] == 'back' :
        if len(que) == 0 : print(-1)
        else : print(que[-1])
