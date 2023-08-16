import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

def make_formula(index, result, add, sub, mul, div):
    global max_result, min_result
    if index == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    if add != 0:
        make_formula(index + 1, result + num[index], add - 1, sub, mul, div)
    if sub != 0:
        make_formula(index + 1, result - num[index], add, sub - 1, mul, div)
    if mul != 0:
        make_formula(index + 1, result * num[index], add, sub, mul - 1, div)
    if div != 0:
        make_formula(index + 1, int(result / num[index]), add, sub, mul, div - 1)

max_result = -(sys.maxsize-1)
min_result = sys.maxsize
make_formula(1, num[0], add, sub, mul, div)
print(max_result)
print(min_result)