import sys
input = sys.stdin.readline

if __name__ == "__main__":
    num_x = 1 # 1 ~ 99 모두 등차수열을 이룸

    n = int(input())

    for i in range(100, n+1): # 세 자리 수만 검사
        hundred = i//100
        ten = i%100//10
        one = i%100%10
        if ten - hundred == one - ten :
            num_x += 1

    print(num_x)