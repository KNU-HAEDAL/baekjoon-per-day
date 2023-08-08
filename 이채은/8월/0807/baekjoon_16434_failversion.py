N, A = map(int, input().split())
arr = []
for _ in range(N):
  type, atk, hp = map(int, input().split())
  arr.append((type, atk, hp))

def clearprob(curATK, maxHP):
  curHP = maxHP
  for type, atk, hp in arr:
    if type == 1:
      turn = hp // curATK if not hp % curATK else hp // curATK + 1
      curHP -= atk * (turn - 1)
    else:
      curATK += atk
      curHP += hp
      if curHP > maxHP:
        curHP = maxHP
    if curHP <= 0:
      return False
  return True

result = 0
start, end = 1, N * int(1e6) * int(1e6)
while start <= end:
  mid = (start + end) // 2
  if clearprob(A, mid):
    end = mid - 1
    result = mid
  else:
    start = mid + 1

print(result)
