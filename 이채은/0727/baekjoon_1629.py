def dac(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (dac(a,b//2,c)**2)%c
    else:
        return ((dac(a,b//2,c)**2)*a)%c

ABC = list(map(int, input().split()))
print(dac(ABC[0], ABC[1], ABC[2]))
