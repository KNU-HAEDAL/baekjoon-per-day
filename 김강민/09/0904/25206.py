import sys
input = sys.stdin.readline

grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

score_total = 0
total = 0

for _ in range(20):
    subject, s, g = input().split()
    s = float(s)
    if g != 'P':
        score_total += s
        total += s * score[grade.index(g)]

print(round(total / score_total, 6))