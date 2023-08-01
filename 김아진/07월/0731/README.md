# 0731 - 분할정복


### [Silver IV] [치킨 TOP N](https://www.acmicpc.net/problem/11582) - 11582 

> <p>합병 정렬로 치킨 집 순위를 정렬하던 중 문득 민호는 작업의 중간단계가 궁금해졌다. 현재 단계에서 k명의 회원이 정렬을 진행할 때 정렬을 마친 뒤 결과를 출력해라.</p>

#### 풀이
<img src="https://velog.velcdn.com/images/ppocchi/post/a788d0d1-ed32-42c8-a5f6-587f957bdc5d/image.png">

일반적인 합병정렬 진행 중
1. k == n<sup>depth</sup>
(지금이 k 단계)라면 지금 쪼개진 상태에서 각각 정렬하고 합친 치킨집 리스트 리턴
2. k != n<sup>depth</sup> 
라면 계속 쪼개기

#### 다른 풀이

정렬시킬 원소의 개수를 n에서 k를 나누어 구하고 치킨집을 처음부터 돌면서 원소의 개수만큼 정렬 시키기




### [Gold V] [Moo 게임](https://www.acmicpc.net/problem/5904) - 5904 

> <p>Moo 수열은 다음과 같은 방법으로 재귀적으로 만들 수 있다. 먼저, S(0)을 길이가 3인 수열 "m o o"이라고 하자. 1보다 크거나 같은 모든 k에 대해서, S(k)는 S(k-1)과 o가 k+2개인 수열 "m o ... o" 와 S(k-1)을 합쳐서 만들 수 있다. N이 주어졌을 때, Moo 수열의 N번째 글자를 구하는 프로그램을 작성하시오.</p>

#### 풀이

<img src="https://velog.velcdn.com/images/ppocchi/post/b85623f3-286f-4f53-8522-eb62888b628c/image.png">

- n의 값이 매우 크기때문에 직접 수열을 구해 n번째 글자를 구하기는 불가능 → 규칙을 찾아 분할정복

1. n과 제일 인접한 최대 크기의 S(k) 길이(length)와 k 구하기
2. k, length로 재귀 돌면서 n번째 수 구하기
    - 수열은 총 3부분(k-1번째 수열, k번째 moo부분, k-1번째 수열)으로 나누기 가능
    - 첫 번째 부분이라면 S(k-1)로 분할, 두 번째라면 글자 리턴, 세 번째 부분이라면 S(k-1)로 분할하고 n도 변경




### # [Gold I] [트리의 순회](https://www.acmicpc.net/problem/2263) - 2263 

> <p>n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다. 이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하시오.</p>

#### 풀이

<img src="https://velog.velcdn.com/images/ppocchi/post/6133a219-7bcd-4378-b450-98e0f018659b/image.png" width="80%">

1. 지금 preorder의 node는 지금 postorder의 맨 끝 원소
2. inorder에서 앞에서 구한 node 기준으로 왼쪽, 오른쪽 원소로 preorder 쪼개기

    - 지금 inorder에서 node의 위치(index) 찾기
    - 왼쪽: 지금 inorder의 시작점 ~ index - 1
    - 오른쪽: index + 1 ~ 지금 inorder의 끝점

3. 지금 postorder의 크기가 0일 때 까지 반복