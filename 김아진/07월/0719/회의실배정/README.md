# [Silver I] 회의실 배정 - 1931
[문제 링크](https://www.acmicpc.net/problem/1931)

### 성능 요약
메모리: 52036 KB, 시간: 236 ms

### 분류
그리디 알고리즘, 정렬

### 문제 설명
<p>한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.</p>

### 입력
<p>첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 2<sup>31</sup>-1보다 작거나 같은 자연수 또는 0이다.</p>

### 출력
<p>첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.</p>

# 문제 접근
<img src="https://velog.velcdn.com/images/ppocchi/post/c21520cf-9b16-4f46-adc9-d2effa26ebe7/image.png" width="100%">

>모든 회의 시간 보면서 T(최근에 끝난 회의 시간)와 현재의 회의 시작 시간 비교

1. e(회의 끝나는 시간) 오름차순으로 정렬하기
- "사용가능한 회의의 최대 개수"에서 greedy 문제로 판단해 정렬하고 시작
- for문을 돌 때, T값을 업데이트 하면서 순차적으로 비교하기 때문에 끝나는 시간을 기준으로 정렬
2. for문 돌면서 최근에 끝난 **회의 시간(T)**과 **현재 시작할 회의 시간(s[i])** 비교
- T ≤ s[i]이면, 회의 개수 추가하고 T값 현재 회의 끝나는 시간으로 업데이트

# 학습 내용
1. range에 인수 추가해서 for문 초기값 설정 가능
2. key 사용해서 list의 원하는 index 기준으로 정렬 가능