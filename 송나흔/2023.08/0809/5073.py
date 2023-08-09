import sys

while True:
    x = []
    a, b, c = map(int, sys.stdin.readline().split())
    if (a == 0) and (b == 0) and (c == 0):
        break

    x.append(a)
    x.append(b)
    x.append(c)
    x.sort()

    if x[2] >= (x[1] + x[0]):
        print("Invalid")
    else:
        if (a == b) and (a == c):
            print("Equilateral")
        elif (a == b) or (a == c) or (b == c):
            print("Isosceles")
        else:
            print("Scalene")