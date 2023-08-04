num = []
sum = 0
for i in range(5):
    num.append(int(input()))
    sum += num[i]

num.sort()
print(int(sum / 5))
print(num[2])