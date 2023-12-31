# 8월 18일

[마법사 상어와 파이어볼](https://www.acmicpc.net/problem/20056)  

## 문제 설명
크기가 N×N인 격자에 파이어볼 M개를 발사했다. 가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다. i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si이다. 위치 (r, c)는 r행 c열을 의미한다.

격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.

마법사 상어가 모든 파이어볼에게 이동을 명령하면 다음이 일들이 일어난다.

1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
  - 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
  1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
  2. 파이어볼은 4개의 파이어볼로 나누어진다.
    - 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
    - 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
    - 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
    - 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
3. 질량이 0인 파이어볼은 소멸되어 없어진다.

마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.

## 해설
- 구현
- 시뮬레이션

간단한 구현 문제이다. 1번 행과 N번 행이 연결되어 있고, 1번 열과 N번 열이 연결되어 있다는 것을 기억하자.