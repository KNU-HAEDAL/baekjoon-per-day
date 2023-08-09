N, M = map(int, input().split())
package = []
single = []

for _ in range(M):
    a, b = map(int, input().split())
    package.append(a)
    single.append(b)

min_package = min(package)
ans = 0

while N > 0:
    if N >= 6:
        min_single = min(single)*6
        N -= 6
    else:
        min_single = min(single)*N
        N -= N
    if min_single < min_package:
        ans += min_single
    else:
        ans += min_package

print(ans)
