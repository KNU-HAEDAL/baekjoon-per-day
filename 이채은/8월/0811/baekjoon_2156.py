N = int(input())
array = [0]*10000
for i in range(N):
  array[i] = int(input())

dks = [0]*10000
dks[0] = array[0]
dks[1] = array[0] + array[1]
dks[2] = max(array[2] + array[0], array[2] + array[1], dks[1])
for i in range(3,N):
  dks[i]=max(array[i] + dks[i-2], array[i] + array[i-1] + dks[i-3], dks[i-1])

print(max(dks))
