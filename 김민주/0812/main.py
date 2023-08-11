x = (input())
cro_language = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in cro_language:
    x = x.replace(i, 'x')
print(len(x))
