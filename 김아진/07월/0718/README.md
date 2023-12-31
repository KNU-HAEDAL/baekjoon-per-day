# 7월 18일
## [Gold V] 강의실 배정 - 11000 

[문제 링크](https://www.acmicpc.net/problem/11000) 

### 성능 요약

메모리: 61296 KB, 시간: 332 ms

### 분류

자료 구조, 그리디 알고리즘, 우선순위 큐, 정렬

### 문제 설명

<p>수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. </p>

<p>김종혜 선생님한테는 S<sub>i</sub>에 시작해서 T<sub>i</sub>에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. </p>

<p>참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, T<sub>i</sub> ≤ S<sub>j</sub> 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)</p>

<p>수강신청 대충한 게 찔리면, 선생님을 도와드리자!</p>

### 입력 

 <p>첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)</p>

<p>이후 N개의 줄에 S<sub>i</sub>, T<sub>i</sub>가 주어진다. (0 ≤ S<sub>i</sub> < T<sub>i</sub> ≤ 10<sup>9</sup>)</p>

### 출력 

 <p>강의실의 개수를 출력하라.</p>

## 문제 접근
<img src="https://velog.velcdn.com/images/ppocchi/post/cc3cc3ac-5b85-4935-afb9-a98244c37bb5/image.png" width="100%">

>모든 수업의 시간을 보면서 현재 수업의 S와 강의실 배정 받은 강의의 T 비교

1. S 오름차순으로 정렬하기
- "최소의 강의실 개수를 구하는"에서 greedy 문제로 판단해 정렬하고 시작
- for문을 돌면서 현재 강의의 S를 보기 때문에 S 기준으로 정렬
2. 강의실 추가 or 강의 추가 나누기
- T > s[i]: 강의실 추가, 해당 강의의 T 추가
- T ≤ s[i]: T 업데이트(기존 T 삭제, 해당 강의의 T 추가)
3. T를 priority queue로 처리하기
<img src="https://velog.velcdn.com/images/ppocchi/post/172a2786-3f93-4dc8-9457-c4b08a482729/image.png" width="100%">
- T를 리스트로 만들어 오름차순으로 정렬하고 맨 앞의 값만 비교 → priority queue 사용

## 학습 내용
1. 입력 받을 때 sys사용하면 엄청 빨라짐
2. map으로 입력 2개 받기
3. 파이썬에서 pq는 heapq 사용(heapq가 priority queue보다 더 빠르다)
