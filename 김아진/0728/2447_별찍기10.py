import sys
input = sys.stdin.readline

def print_star(n):
    if n == 1:
        return ["*"]

    sqaure = print_star(n//3)
    star = []
    for i in sqaure:
        star.append(i*3)
    for i in sqaure:
        star.append(i + ' ' * (n//3) + i)
    for i in sqaure:
        star.append(i*3)
    
    return star

n = int(input())
print_star(n)
print('\n'.join(print_star(n)))