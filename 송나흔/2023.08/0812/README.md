# 23.08.12

## [Bronze II] 알고리즘 수업 - 알고리즘의 수행 시간 6 - 24267 

[문제 링크](https://www.acmicpc.net/problem/24267) 

### 성능 요약

메모리: 31256 KB, 시간: 44 ms

### 분류

구현, 수학, 시뮬레이션

### 문제 설명

<p>오늘도 서준이는 알고리즘의 수행시간 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p>입력의 크기 <em>n</em>이 주어지면 MenOfPassion 알고리즘 수행 시간을 예제 출력과 같은 방식으로 출력해보자.</p>

<p>MenOfPassion 알고리즘은 다음과 같다.</p>

<pre>MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}</pre>

### 입력 

 <p>첫째 줄에 입력의 크기 <em>n</em>(1 ≤ <i>n</i> ≤ 500,000)이 주어진다.</p>

### 출력 

 <p>첫째 줄에 코드1 의 수행 횟수를 출력한다.</p>

<p>둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다. 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.</p>

---
### 풀이

- n = 7 이라고 할 때, 제일 바깥쪽 for문은 1 ~ 5까지 수행됨.
- i = 1 일 때, 두 번째 for문은 2 ~ 6까지 수행됨.
- j = 2 일 때, 세 번째 for문은 3 ~ 7까지 수행됨.
- i와 j값이 오를 때마다 j와 k도 영향을 받아 같이 범위가 올라가게 되므로, 중복되지 않는 숫자를 선택하는 조합 공식을 사용하면 됨.
    - nC3 = n! / ((n - 3)! * 3!) = (n * (n - 1) * (n - 2)) / 6