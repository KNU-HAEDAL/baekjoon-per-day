# 0809 - 완전탐색(DFS)

### [Gold IV] [테트로미노](https://www.acmicpc.net/problem/14500) - 14500 


<p>폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.</p>

<ul>
	<li>정사각형은 서로 겹치면 안 된다.</li>
	<li>도형은 모두 연결되어 있어야 한다.</li>
	<li>정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.</li>
</ul>

<p>정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.</p>

<p style="text-align:center"><a href="https://commons.wikimedia.org/wiki/File:All_5_free_tetrominoes.svg"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14500/1.png" style="height:167px; width:250px"></a></p>

<p>아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.</p>

<p>테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.</p>

### 풀이
다음 그림처럼 (0,0) 위치에서 깊이가 4일 때까지 백트래킹 돌리면 테트로미노 형태를 만들 수 있다. 단, (ㅏ,ㅓ,ㅗ,ㅜ)의 모양은 깊이가 2일 때 중복처리를 해야 나오기 때문에 따로 함수를 만들어 처리한다.

<src img="https://velog.velcdn.com/images/ppocchi/post/91178a38-f641-417b-ba7b-41fd3eba4948/image.png">