word = list(input().upper())
arr = []
for i in range(ord("A"),ord("Z")+1):
    arr.append(word.count(chr(i)))
if arr.count(max(arr)) != 1 :
    print("?")
else:
    print(chr(arr.index(max(arr))+65))

