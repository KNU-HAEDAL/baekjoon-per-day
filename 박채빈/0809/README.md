# 8월 9일

[수 찾기](https://www.acmicpc.net/problem/1920)

## 문제 해결
vector가 일반배열보다 자동으로 길이가 길어져서 편하지만 더 느리다(배열로하면 괜찮지만 vector쓰면 시간초과뜸)
endl보다는 \n을 사용하는것이 더 빠르다.
ios_base::sync_with_stdio(0);cin.tie(0); 이 부분에서 잘못사용하면 원하는 순서로 안나온다길래 안사용했더니 이걸 안하면 무조건 시간초과뜬다。 사용하기 싫은데  scanf밖에 답이 없어서 그게 더 싫어서 포기했다. 
문제 자체는 쉬운데 시간을 줄이는 게 너무 오랜 시간이 걸렸다.

## 참고자료
[c qsort vs cpp sort()](https://underflow101.tistory.com/45)
[sort 사용법](https://blockdmask.tistory.com/178)
[중복되는 원소 없애기(unique)](https://dpdpwl.tistory.com/39)
[이분탐색 함수 binary_search()](https://m42-orion.tistory.com/69)
[입력 속도 비교](https://www.acmicpc.net/blog/view/56)