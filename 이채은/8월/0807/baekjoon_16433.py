N, R, C = map(int, input().split())
field = [['.']*N for _ in range(N)]
field[R-1][C-1] = 'v'

for row in range(N):
  if (R+C) % 2 == 0:
    if row % 2 == 0:
      for column in range(0,N,2):
        field[row][column] = 'v'
    else: 
      for column in range(1,N,2):
        field[row][column] = 'v'
  else:
    if row % 2 == 0:
      for column in range(1,N,2):
        field[row][column] = 'v'
    else:
      for column in range(0,N,2):
        field[row][column] = 'v'

for f in field:
  print(''.join(f))
