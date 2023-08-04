N, M = map(int, input().split())
book_list = list(map(int, input().split()))
possector, negsector = [0], [0]

for num in book_list :
  if num > 0 :
    possector.append(num)
  else :
    negsector.append(-num)

possector.sort()
negsector.sort()
max_val = max(possector[-1], negsector[-1])
result = 0

while possector :
  result += possector[-1] * 2
  count = 0
  while possector and count < M :
    count += 1
    possector.pop()

while negsector :
  result += negsector[-1] * 2
  count = 0
  while negsector and count < M :
    count += 1
    negsector.pop()

print(result - max_val)
