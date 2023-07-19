# [Silver I] 단지번호붙이기 - 2667 

[문제 링크](https://www.acmicpc.net/problem/2667) 

### 성능 요약

메모리: 31332 KB, 시간: 44 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 문제 설명

<p><그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images/ITVH9w1Gf6eCRdThfkegBUSOKd.png" style="height:192px; width:409px"></p>

### 입력 

 <p>첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.</p>

### 출력 

 <p>첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.</p>


# 문제 풀이(bfs)
### 문제 접근
<img src="https://velog.velcdn.com/images/ppocchi/post/a4ff7569-cc23-48aa-870b-9668cd5866f7/image.png" width="80%">

> graph 돌면서 값이 1이면 queue에 넣어 상하좌우 방문하기 → bfs

### 풀이
<img src="https://velog.velcdn.com/images/ppocchi/post/e2ed83ca-a66e-468c-a596-614e32414313/image.png" width="80%">

1. bfs 들어오면 home 개수 초기화하기
2. (i,j)를 queue에 넣고 visit 처리하기
3. queue가 비어 있을 때까지 while문 돌기
	**(i,j)의 상하좌우를 for문으로 처리**
    1. queue의 (i,j)값 비우기
    2. cur_i, cur_j 값 설정하기
    	- cur_i = v[0] + dir[0]
        - cur_j = v[1] + dir[1]
    3. cur_i, cur_j가 graph 경계 벗어나는지 체크
    	- (cur_i < 0) or (cur_i ≥ n)
    4. (cur_i, cur_j)의 graph 값이 1이고 visit 안했다면
    	1. home 개수 1 증가
        2. queue에 (cur_i, cur_j) 넣고 visit 처리
    	
# 문제 풀이(dfs)
### 문제 접근
> 굳이 queue를 써야할까.... 그냥 그래프 다 돌면서 방문 안한 것만 처리

### 풀이
<img src="blob:https://velog.io/48a926c9-b598-4e21-b879-f95139777f13" width="80%">

# 학습 내용
1. 입력 여러 줄 한번에 받을 때 rstrip 사용하기
2. list(map...)해서 한 줄 입력을 따로따로 리스트에 넣을 수 있다!!!!