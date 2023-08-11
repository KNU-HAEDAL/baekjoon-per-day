import sys
input = sys.stdin.readline
answer = 0

def select_day(today, fin_day, total):
    global answer
    if today > n:
        answer = max(answer, total)
        return
    
    if fin_day < today:
        if end_day[today] <= n:
            select_day(today + 1, end_day[today], total + price[today])
    select_day(today + 1, fin_day, total)
    

n = int(input())
start_day = [0]
end_day = [0]
price = [0]
for today in range(1, n+1):
    t, p = map(int, input().split())
    start_day.append(t)
    end_day.append(t + today - 1)
    price.append(p)

select_day(1, 0, 0)
print(answer)