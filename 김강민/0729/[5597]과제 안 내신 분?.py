student = [i for i in range(1, 31)]

for _ in range(28):
    submit = int(input())
    student.remove(submit)

student.sort()
print(student[0])
print(student[-1])
