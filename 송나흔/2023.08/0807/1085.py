x, y, w, h = map(int, input().split())

a = (w - x) if (w - x) < (x - 0) else (x - 0)
b = (h - y) if (h - y) < (y - 0) else (y - 0)

if a < b:
    print(a)
else:
    print(b)