import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
operation = list(map(int, input().split()))
op_list = set()

def make_op_list(index, op_str):
    if index == n - 1:
        op_list.add(op_str)
        return
    for i in range(4):
        if operation[i] != 0:
            operation[i] -= 1
            make_op_list(index + 1, op_str + str(i))
            operation[i] += 1
        
make_op_list(0, '')

max_ex = -(sys.maxsize - 1)
min_ex = sys.maxsize
for op in op_list:
    expression = num[0]
    for i in range(n-1):
        if op[i] == '0':
            expression += num[i+1]
        elif op[i] == '1':
            expression -= num[i+1]
        elif op[i] == '2':
            expression *= num[i+1]
        else:
            if expression < 0:
                expression = -(-expression // num[i+1])    
            else:
                expression //= num[i+1]
    max_ex = max(expression, max_ex)
    min_ex = min(expression, min_ex)

print(max_ex)
print(min_ex)