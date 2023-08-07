x_square = list()
y_square = list()
for _ in range(3):
    x, y = map(int, input().split())
    x_square.append(x)
    y_square.append(y)

for i in range(3):
    if x_square.count(x_square[i]) == 1:
        x_ans = x_square[i]
    if y_square.count(y_square[i]) == 1:
        y_ans = y_square[i]

print(x_ans, y_ans)