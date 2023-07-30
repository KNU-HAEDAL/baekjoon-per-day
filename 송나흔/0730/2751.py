import sys
N = int(sys.stdin.readline())
A = list()

for i in range(N):
    num = int(sys.stdin.readline())
    A.append(num)

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged_arr = []

    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1
    merged_arr += left[l:]
    merged_arr += right[r:]
    return merged_arr

A_sorted = merge_sort(A)
for i in range(N):
    print(A_sorted[i])