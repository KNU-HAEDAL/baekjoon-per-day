def solution(n):
    fac = 1
    answer = 1
    while fac <= n:
        answer += 1
        fac *= answer
    answer -= 1
    return answer