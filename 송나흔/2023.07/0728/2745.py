N, B = input().split()

sum = 0
length = len(N)
for i in range(length):
    if ord(N[i]) < 58:
        sum += int(N[i]) * (int(B) ** (length - 1 - i))
    else:
        sum += (ord(N[i]) - 55) * (int(B) ** (length - 1 - i))

print(sum)