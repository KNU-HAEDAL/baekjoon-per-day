import sys
input = sys.stdin.readline

n = int(input())

def moo(i, l, n):
    pre_l = (l - (i+3)) // 2

    if n <= pre_l:
        return moo(i-1, pre_l, n)
    elif n > pre_l + (i+3):
        return moo(i-1, pre_l, n - (pre_l + (i+3)))
    else:
        if pre_l + 1 == n:
            return 'm'
        else:
            return 'o'
i = 0
k = 3
while n > k:
    i += 1
    k = 2*k + (i+3)

print(moo(i,k,n))