# 8월 17일

[CD](https://www.acmicpc.net/problem/4158)

## 문제 해결
<p>처음에 이해를 못해서 왜 마지막에 0 0을 입력하는건지 몰라서 cin>>tmp>>tmp; 로 때웠는데 알고보니 0 0을 입력할때까지 반복하는 거였다. 처음에는 find함수를 사용해서 단순하게 하고싶었는데 시간복잡도가 O(N)이라서 십억을 돌리는거라 10초정도가 걸린다고 한다. 그래서 인덱스 1개1개를 비교하며 마지막까지 비교했다.</p>

## 참고자료
+ [find함수 사용법](https://www.techiedelight.com/ko/check-vector-contains-given-element-cpp/)
+ [find 시간복잡도](https://hibee.tistory.com/48)