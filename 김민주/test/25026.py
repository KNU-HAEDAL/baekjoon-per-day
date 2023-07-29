score = {'A+':4.5, 'A0':4.0 , 'B+':3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+': 1.5, 'D0' : 1.0 , 'F' : 0.0 }
div = 0
result = 0
for i in range(20):
    a = list(input().split(" "))
    a[1] = float(a[1])
    if a[2] == 'P':
        div -= 0
    else:
        sub = float(score[a[2]])
        result += a[1] * sub
        div += a[1]
print(result/div)