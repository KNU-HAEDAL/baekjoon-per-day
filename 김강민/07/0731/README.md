# 7월 30일

## [브론즈 4] 11720 - 숫자의 합

[문제 보러가기]
https://www.acmicpc.net/problem/11720

## 문제 설명

N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

### 꼭 알아야하는 것

-   리스트
-   sys.stdin.readline()
-   map
-   sum함수로 더해버리기

## 해설

1.  N을 입력받는다
2.  list에 숫자들을 입력받는다.
3.  sum()으로 list의 숫자들을 모두 더한다.

## 잡담
map에다가 readline()을 쓰니까 int형 오류가 계속 발생한다.
둘은 같이 쓰면 안되는것 같다.
파이썬은 sum()으로 한번에 다 더할수 있다.
c는 다 쪼개고... 합치고.. 더하고 했는데... 파이썬 쨩!