"""
<게임 규칙>
플레이어는 매 턴마다 숫자를 입력하며, 입력된 숫자들은 공백(space)로 구분합니다.
플레이어와 컴퓨터 모두 한 번의 턴에서 최대 3개의 숫자를 외칠 수 있습니다.
숫자를 외칠 때에는 이전에 외쳐진 숫자보다 1 큰 수만 외칠 수 있습니다.
예를 들어, 컴퓨터가 마지막 숫자로 7을 외쳤다면, 플레이어는 7을 이어서 8, 9, 10 까지 외칠 수 있습니다.
컴퓨터도 동일한 규칙을 따라야 합니다.
'31'이라는 숫자가 나오면 게임을 종료합니다.
"""

import random

current_number = [0, 0]

def bs31():
    print("베스킨라빈스 31 게임")
    print("------------------")

    game = True
    computer_number = 0

    while game:
        if computer_number >= 30:
            print("컴퓨터의 승리")
            game = False
            break

        my = list(map(int, input("My turn - 숫자를 입력하세요: ").split()))
        
        if my[-1] == 30:
            print("당신의 승리")
            game = False
            break

        current_number[0] = my[-1]
        print(f"현재숫자: {current_number[0]}\n")

        computer_turn_num = random.randint(1, 3)

        print("컴퓨터 :", end = " ")
        for i in range(1, computer_turn_num + 1):
            computer_number = int(my[-1] + i)

            print(computer_number, end = " ")
        
        print()
        
        current_number[1] = computer_number

        print(f"현재숫자: {current_number[1]}")
        print("------------------")

bs31()