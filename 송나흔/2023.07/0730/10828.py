import sys
N = int(sys.stdin.readline())
stack_A = list()

for i in range(N):
    inst = sys.stdin.readline().split()

    if inst[0] == "push":
        stack_A.append(inst[1])
    elif inst[0] == "pop":
        if len(stack_A) == 0:
            print(-1)
        else:
            print(stack_A.pop())
    elif inst[0] == "size":
        print(len(stack_A))
    elif inst[0] == "empty":
        if len(stack_A) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack_A) == 0:
            print(-1)
        else:
            print(stack_A[-1])