import sys
input = sys.stdin.readline

n = int(input())
chicken = list(map(int, input().split()))
k = int(input())

def sort_chicken(nums, depth):
    if len(nums) == 1:
        return nums
    
    m = len(nums) // 2
    left = nums[:m]
    right = nums[m:]

    if k != 2**depth:
        return sort_chicken(left, depth+1) + sort_chicken(right, depth+1)
    else:
        c = left + right
        c.sort()
        return c

print(*sort_chicken(chicken, 0))