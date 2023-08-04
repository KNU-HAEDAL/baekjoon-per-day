A, B = map(int, input().split())
C, D = map(int, input().split())
E, F = map(int, input().split())

bessie = max(abs(E-A), abs(F-B))
daisy = abs(E-C)+abs(F-D)

if bessie == daisy:
  print("tie")
elif daisy > bessie:
  print("bessie")
else:
  print("daisy")
