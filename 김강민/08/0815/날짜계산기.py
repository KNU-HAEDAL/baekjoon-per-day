"""
<요구사항>

1. 사용자로부터 날짜와 요일을 입력받습니다.
2. "오늘부터 1일"이기 때문에, 입력한 날짜를 하루로 포함하여 계산합니다.
3. 연도는 구분하지 않으며, 윤년을 고려하지 않고 2월은 항상 28일로 가정합니다.
4. 계산 결과는 "100일 뒤의 날짜는 X월 X일 X요일입니다." 라는 메세지와 함께 출력합니다.
"""

def input_date():
    while True:
        date = input("날짜(월/일)를 입력하세요 (예. 6/21): ")
        month, day = date.split("/")
        month, day = int(month), int(day)
        
        if month < 1 or month > 12:
            print("1~12월 중 하나를 입력해주세요.")
            continue
        if day < 1 or day > 31:
            print("1~31일 중 하나를 입력해주세요.")
            continue
        
        weekday = input("요일을 입력하세요 (예. 월): ")
        return month, day, weekday

def calculate_month_day(month, day, days):
    month_day_map = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    day += days
    while day > month_day_map[month]:
        day -= month_day_map[month]
        month += 1
        if month > 12:
            month = 1
    return month, day

def calculate_weekday(weekday, days):
    day_map = {
        "월": 0,
        "화": 1,
        "수": 2,
        "목": 3,
        "금": 4,
        "토": 5,
        "일": 6
    }
    weekdays = ["월", "화", "수", "목", "금", "토", "일"]
    start_day = day_map[weekday]
    end_day = (start_day + days) % 7
    return weekdays[end_day]

def after_100():
    month, day, weekday = input_date()
    month, day = calculate_month_day(month, day, 100)
    weekday = calculate_weekday(weekday, 100)
    print(f"우리의 기념일은 {month}월 {day}일 {weekday}입니다.")
    print(f"이로부터 100일 뒤의 날짜는 {month}월 {day+100}일 {calculate_weekday(weekday, 100)}입니다.")

after_100()
