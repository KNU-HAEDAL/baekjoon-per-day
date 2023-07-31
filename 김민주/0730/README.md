# 프로그래머스 [배열 뒤집기] ;LEVEL 0

<https://school.programmers.co.kr/learn/courses/30/lessons/120821>

## Python의 리스트/배열 역순 정렬 : _reverse(), reversed(list)_

1. `list.reverse()` : list자체를 역순으로 정렬, 함수 반환값 : NUll

- 반환값이 Null이기 때문에 rev = list.reverse() 실행 시 rev = Null
- 따라서 list.reverse()하면 list 자체가 역순으로 정렬됨

ex) list = [1,2,3] / list.reverse() / 출력 : list = [3,2,1]

2. `reversed(list)` : 반환값이 배열임 -> 다른 변수에 저장 가능, 변수수정x

ex) list = [1,2,3] / list2 = reverse(list) / 출력: list2 = [3,2,1]
