# 0811 - 구현, 완전탐색, 그리디

### [Gold V] [로봇 청소기](https://www.acmicpc.net/problem/14503) - 14503

<li>현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.</li>
	<li>현재 칸의 주변 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container>칸 중 청소되지 않은 빈 칸이 없는 경우,
	<ol>
		<li>바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.</li>
		<li>바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.</li>
	</ol>
	</li>
	<li>현재 칸의 주변 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container>칸 중 청소되지 않은 빈 칸이 있는 경우,
	<ol>
		<li>반시계 방향으로 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mo class="mjx-n" size="s"><mjx-c class="mjx-c2218"></mjx-c></mjx-mo></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>90</mn><mo>∘</mo></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$90^\circ$</span></mjx-container> 회전한다.</li>
		<li>바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.</li>
		<li>1번으로 돌아간다.</li>
	</ol>
	</li>
</ol>

### 풀이

문제에서 주어진 조건 그대로 구현하면 되는 문제, 딱히 까다로운 조건이 없어 쉽다 ㅎㅎ,,

<br>
<br>

### [Silver III] [퇴사](https://www.acmicpc.net/problem/14501) - 14501

<p>상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.</p>

<p>오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.</p>

<p>백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.</p>

<p>각각의 상담은 상담을 완료하는데 걸리는 기간 T<sub>i</sub>와 상담을 했을 때 받을 수 있는 금액 P<sub>i</sub>로 이루어져 있다.</p>

<p>N = 7인 경우에 다음과 같은 상담 일정표를 보자.</p>

<table class="table table-bordered">
	<thead>
		<tr>
			<th> </th>
			<th>1일</th>
			<th>2일</th>
			<th>3일</th>
			<th>4일</th>
			<th>5일</th>
			<th>6일</th>
			<th>7일</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th>T<sub>i</sub></th>
			<td>3</td>
			<td>5</td>
			<td>1</td>
			<td>1</td>
			<td>2</td>
			<td>4</td>
			<td>2</td>
		</tr>
		<tr>
			<th>P<sub>i</sub></th>
			<td>10</td>
			<td>20</td>
			<td>10</td>
			<td>20</td>
			<td>15</td>
			<td>40</td>
			<td>200</td>
		</tr>
	</tbody>
</table>

<p>1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다. 5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.</p>

<p>상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다. 예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다. 2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.</p>

<p>또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.</p>

<p>퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.</p>

<p>상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.</p>

### 풀이
n이 15이하여서 총 날짜를 다 돌아보면서 하루마다 선택 하거나 안하거나 했을 때의 경우를 보면 된다. 
날짜를 선택할 때 현재 날짜가 앞의 상담 종료 날짜보다 큰 경우, 현재 날짜의 상담 종료 날짜가 총 날짜를 넘지 않는 경우만 날짜 선택이 가능하게 한다.

<br>
<br>

### [Bronze II] [시험 감독](https://www.acmicpc.net/problem/13458) - 13458


<p>총 N개의 시험장이 있고, 각각의 시험장마다 응시자들이 있다. i번 시험장에 있는 응시자의 수는 A<sub>i</sub>명이다.</p>

<p>감독관은 총감독관과 부감독관으로 두 종류가 있다. 총감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 B명이고, 부감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 C명이다.</p>

<p>각각의 시험장에 총감독관은 오직 1명만 있어야 하고, 부감독관은 여러 명 있어도 된다.</p>

<p>각 시험장마다 응시생들을 모두 감시해야 한다. 이때, 필요한 감독관 수의 최솟값을 구하는 프로그램을 작성하시오.</p>