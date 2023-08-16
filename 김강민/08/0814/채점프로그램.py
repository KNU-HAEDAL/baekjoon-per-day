# 학생 답
s = ["김갑,3242524215",
    "이을,3242524223",
    "박병,2242554131",
    "최정,4245242315",
    "정무,3242524315"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

def grader(student_ans, true_ans):
    student_score = []
    for ans in student_ans:
        name, answer = ans.split(",")
        score = 0
        for i in range(len(answer)):
            if int(answer[i]) == true_ans[i]:
                score += 10
        student_score.append((name, score))

    student_score.sort(key=lambda x: x[1], reverse=True)
    rank = 1
    for i in range(len(student_score)):
        score = student_score[i]
        print(f"학생: {score[0]} 점수: {score[1]}점 {rank}등")
        if i < len(student_score)-1 and score[1] != student_score[i+1][1]:
            rank += 1

grader(s, a)
