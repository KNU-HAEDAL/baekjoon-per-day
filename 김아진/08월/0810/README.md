# 0810 - 구현, 완전탐색

### [Gold IV] [뱀](https://www.acmicpc.net/problem/3190) - 3190

<p> 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.</p>

<p>게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.</p>

<p>뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.</p>

<ul>
	<li>먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.</li>
	<li>만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.</li>
	<li>만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.</li>
	<li>만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.</li>
</ul>

<p>사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.</p>

### 풀이

while문으로 1초씩 증가하면서 뱀 이동하기
1. 딕셔너리에 저장한 방향 전환 시간과 현재 시간이 같다면 해당 방향으로 바꾸기

    - 방향은 dx, dy로 구현
    - 뱀의 머리 방향에 따라 L, R의 방향이 달라짐
    
    <img src="https://velog.velcdn.com/images/ppocchi/post/d8bb815a-353e-41b2-a48e-ab836ba0aff1/image.png">

2. 다음 위치로 이동하고 종료 조건 체크 후 해당 위치에 사과가 없다면 꼬리를 한 칸 앞으로 당기기

    - snake라는 리스트를 만들어 뱀의 위치 저장해놓고 사과가 없을 땐 리스트의 맨 앞 제거

3. 사과 유무에 상관없이 머리를 다음 위치로 이동하기

<br>
---
<br>

### [Gold II] [2048 (Easy)](https://www.acmicpc.net/problem/12100) - 12100 

# 문제 설명

<p>2048 게임은 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다. 이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다. 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.</p>

<p>이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다. 보드의 크기와 보드판의 블록 상태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.</p>

### 내 풀이

입력값이 작고, 4방향을 5번씩 이동하므로 완전탐색으로 풀어도 괜찮다ㅏ,,
1. 5개의 방향을 중복순열로 뽑아 리스트에 저장하고 하나씩 빼면서 board 움직이기
2. 움직이는 방향마다 함수 만들어 처리하기
    - 서쪽으로 이동하는 경우, 왼쪽부터 보면서 현재 인덱스를 감소시킴
    - 현재 인덱스의 board가 0이면 오른쪽에 있는 거 땡겨오고 이어서 다음 위치보기
    - 현재 인덱스의 board가 오른쪽에 있는 값과 같다면 현재 board를 2배하고 오른쪽 값 0으로 만들기
3. 5번 이동 완료하면 board에서 최대값 구해 정답으로 업데이트하기

### 남 풀이

queue에 0이 아닌 값 저장해 놓고 board 리셋시킨 후, while문 돌면서 queue에 있는 값 하나씩 꺼내 저장하기

    - 현재 위치의 board값이 0이라면, 꺼낸 값 현재 위치에 저장
    - queue에서 꺼낸 값이 현재 위치의 board 값과  같다면 merge시키고 다음 위치로 이동하기
    - 위의 두 조건아니면 다음 위치로 이동하고, 꺼낸 값 현재 위치에 저장

중복순열 함수 쓰는 것 보다 직접 재귀함수로 구현하는 게 훨씬 빠르다