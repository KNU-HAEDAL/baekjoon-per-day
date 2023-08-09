import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if (a + b + c) != 180:
    print("Error")
else:
    if (a == b) and (a == c):
        print("Equilateral")
    elif (a == b) or (a == c) or (b == c):
        print("Isosceles")
    else:
        print("Scalene")