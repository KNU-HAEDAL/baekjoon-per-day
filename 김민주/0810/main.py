# programmers [배열 두 배 만들기]
def solution(numbers):
    answer = []
    for each in numbers:
        answer.append(each*2)
    return answer

# programmers [중앙값 구하기]


def solution(array):
    answer = sorted(array)[len(array)//2]
    return answer
