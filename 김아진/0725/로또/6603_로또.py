import sys, itertools
input = sys.stdin.readline

while True:
    line = list(map(int, input().split()))
    n = line[0]
    if n == 0:
        break
    for i in itertools.combinations(line[1:], 6):
        print(* i)
    print()