N = int(input())
M = int(input())

if N == 1:
  print(8*M)
elif 2 <= N <= 4:
  if M % 2 == 0:
    print(4*M + N - 1)
  else:
    print(4*M + 5 - N)
else:
  print(8*M + 4)
