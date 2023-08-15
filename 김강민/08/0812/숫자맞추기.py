"""
<게임 규칙>

1. 게임에서 사용되는 숫자는 숫자는 0부터 100까지의 정수로 한정합니다.
2. 사용자가 입력한 숫자와 컴퓨터가 선택한 숫자를 비교하여,
정답을 맞추지 못한다면 다음과 같은 힌트를 제공합니다.
    - 만약 사용자의 숫자가 정답보다 크다면, "Down!" 이라는 메세지를 출력합니다.
    - 만약 사용자의 숫자가 정답보다 작다면, "Up!"이라는 메세지를 출력합니다.
3. 이전 시도에 입력한 숫자는 "이미 예측에 사용한 숫자입니다."라는 메세지를 출력합니다.
    - 만약 앞선 시도에서 작성한 숫자보다 크거나 작은 경우, 올바른 범위로 예측할 수 있게 가이드합니다.
4. 게임이 종료되면, 정답과 함께 사용자가 정답을 맞추기까지 시도한 횟수를 출력합니다.
"""

import random

def guess_number():
    answer = random.randint(0, 100)
    guess_list = []

    while True: 
        try:
            guess = int(input("숫자를 예측해보세요 : "))
        except ValueError:
            print("숫자로 입력해주세요.")
            continue
        
        if guess < 0 or guess > 100:
            print("0부터 100사이의 숫자로 입력해주세요.")
            continue
        
        if guess in guess_list:
            print("이미 예측에 사용한 숫자입니다. 다시 한번 고민해보세요.")
            continue
        
        guess_list.append(guess)
        
        if guess == answer:
            print(f"정답입니다. {len(guess_list)}차 시도만에 예측에 성공했네요!! 게임을 종료합니다.")
            break
        elif guess < answer:
            print("UP! 다시 한번 고민해보세요.")
        else:
            print("Down! 다시 한번 고민해보세요.")
        
        closest_higher = max(filter(lambda x : x < guess and x not in guess_list, guess_list), default=None, key=lambda x : guess-x)
        closest_lower = min(filter(lambda x : x > guess and x not in guess_list, guess_list), default=None, key=lambda x : x-guess)
        
        if closest_higher is not None:
            print(f"앞선 예측보다 큰 숫자입니다. {closest_higher}보다 큰 수를 고민해보세요.")
        if closest_lower is not None:
            print(f"앞선 예측보다 작은 숫자입니다. {closest_lower}보다 작은 수를 고민해보세요.")
        if closest_higher is None and closest_lower is None:
            print("아직 시도해보지 않은 숫자입니다. 모든 숫자를 골라보세요.")
