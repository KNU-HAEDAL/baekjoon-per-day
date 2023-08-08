import sys
n, atk = map(int, sys.stdin.readline().split())
dungeon=[[] for i in range(n)]
maxHP, curHP, damage = 0, 0, 0

for i in range(n):
    t, a, h = map(int, sys.stdin.readline().split())
    if t==1:
        temp = h % atk
        if temp == 0:
            damage = -(a * (h // atk - 1))
        else:
            damage = -(a * (h // atk))
    else:
        atk += a
        damage = h
    curHP += damage
    if curHP > 0:
        curHP = 0
    maxHP = max(maxHP, abs(curHP))

print(maxHP+1)
