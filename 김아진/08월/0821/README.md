# 0821 - 구현

### [Gold III] [게리맨더링 2](https://www.acmicpc.net/problem/17779) - 17779 

<p>재현시의 시장 구재현은 지난 몇 년간 게리맨더링을 통해서 자신의 당에게 유리하게 선거구를 획정했다. 견제할 권력이 없어진 구재현은 권력을 매우 부당하게 행사했고, 심지어는 시의 이름도 재현시로 변경했다. 이번 선거에서는 최대한 공평하게 선거구를 획정하려고 한다.</p>

<p>재현시는 크기가 N×N인 격자로 나타낼 수 있다. 격자의 각 칸은 구역을 의미하고, r행 c열에 있는 구역은 (r, c)로 나타낼 수 있다. 구역을 다섯 개의 선거구로 나눠야 하고, 각 구역은 다섯 선거구 중 하나에 포함되어야 한다. 선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다. 구역 A에서 인접한 구역을 통해서 구역 B로 갈 수 있을 때, 두 구역은 연결되어 있다고 한다. 중간에 통하는 인접한 구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함된 구역이어야 한다.</p>

<p>선거구를 나누는 방법은 다음과 같다.</p>

<ol>
	<li>기준점 (x, y)와 경계의 길이 d<sub>1</sub>, d<sub>2</sub>를 정한다. (d<sub>1</sub>, d<sub>2</sub> ≥ 1, 1 ≤ x < x+d<sub>1</sub>+d<sub>2</sub> ≤ N, 1 ≤ y-d<sub>1</sub> < y < y+d<sub>2</sub> ≤ N)</li>
	<li>다음 칸은 경계선이다.
	<ol>
		<li>(x, y), (x+1, y-1), ..., (x+d<sub>1</sub>, y-d<sub>1</sub>)</li>
		<li>(x, y), (x+1, y+1), ..., (x+d<sub>2</sub>, y+d<sub>2</sub>)</li>
		<li>(x+d<sub>1</sub>, y-d<sub>1</sub>), (x+d<sub>1</sub>+1, y-d<sub>1</sub>+1), ... (x+d<sub>1</sub>+d<sub>2</sub>, y-d<sub>1</sub>+d<sub>2</sub>)</li>
		<li>(x+d<sub>2</sub>, y+d<sub>2</sub>), (x+d<sub>2</sub>+1, y+d<sub>2</sub>-1), ..., (x+d<sub>2</sub>+d<sub>1</sub>, y+d<sub>2</sub>-d<sub>1</sub>)</li>
	</ol>
	</li>
	<li>경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구이다.</li>
	<li>5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다.
	<ul>
		<li>1번 선거구: 1 ≤ r < x+d<sub>1</sub>, 1 ≤ c ≤ y</li>
		<li>2번 선거구: 1 ≤ r ≤ x+d<sub>2</sub>, y < c ≤ N</li>
		<li>3번 선거구: x+d<sub>1</sub> ≤ r ≤ N, 1 ≤ c < y-d<sub>1</sub>+d<sub>2</sub></li>
		<li>4번 선거구: x+d<sub>2</sub> < r ≤ N, y-d<sub>1</sub>+d<sub>2</sub> ≤ c ≤ N</li>
	</ul>
	</li>
</ol>

<p>아래는 크기가 7×7인 재현시를 다섯 개의 선거구로 나눈 방법의 예시이다.</p>

<table class="table table-bordered" style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 33%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/c144c31e-db45-4094-9c1d-0656a690aef0/-/preview/" style="width: 300px; height: 303px;"></td>
			<td style="width: 33%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/813c38e0-3197-4589-bc96-17d96eb9ed14/-/preview/" style="width: 300px; height: 305px;"></td>
			<td style="width: 34%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/892417dd-b824-4d4e-8bce-2faf341a9f66/-/preview/" style="width: 300px; height: 302px;"></td>
		</tr>
		<tr>
			<td style="width: 33%; text-align: center;">x = 2, y = 4, d<sub>1</sub> = 2, d<sub>2</sub> = 2</td>
			<td style="width: 33%; text-align: center;">x = 2, y = 5, d<sub>1</sub> = 3, d<sub>2</sub> = 2</td>
			<td style="width: 34%; text-align: center;">x = 4, y = 3, d<sub>1</sub> = 1, d<sub>2</sub> = 1</td>
		</tr>
	</tbody>
</table>

<p>구역 (r, c)의 인구는 A[r][c]이고, 선거구의 인구는 선거구에 포함된 구역의 인구를 모두 합한 값이다. 선거구를 나누는 방법 중에서, 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값을 구해보자.</p>

<br>
<br>

### [Gold II] [새로운 게임 2](https://www.acmicpc.net/problem/17837) - 17837 

<p>재현이는 주변을 살펴보던 중 체스판과 말을 이용해서 새로운 게임을 만들기로 했다. 새로운 게임은 크기가 N×N인 체스판에서 진행되고, 사용하는 말의 개수는 K개이다. 말은 원판모양이고, 하나의 말 위에 다른 말을 올릴 수 있다. 체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나로 색칠되어있다.</p>

<p>게임은 체스판 위에 말 K개를 놓고 시작한다. 말은 1번부터 K번까지 번호가 매겨져 있고, 이동 방향도 미리 정해져 있다. 이동 방향은 위, 아래, 왼쪽, 오른쪽 4가지 중 하나이다.</p>

<p>턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것이다. 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동한다. 말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르며 아래와 같다. 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다.</p>

<ul>
	<li>A번 말이 이동하려는 칸이
	<ul>
		<li>흰색인 경우에는 그 칸으로 이동한다. 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓는다.
		<ul>
			<li>A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동한다.</li>
			<li>예를 들어, A, B, C로 쌓여있고, 이동하려는 칸에 D, E가 있는 경우에는 A번 말이 이동한 후에는 D, E, A, B, C가 된다.</li>
		</ul>
		</li>
		<li>빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
		<ul>
			<li>A, B, C가 이동하고, 이동하려는 칸에 말이 없는 경우에는 C, B, A가 된다.</li>
			<li>A, D, F, G가 이동하고, 이동하려는 칸에 말이 E, C, B로 있는 경우에는 E, C, B, G, F, D, A가 된다.</li>
		</ul>
		</li>
		<li>파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동한다. 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.</li>
		<li>체스판을 벗어나는 경우에는 파란색과 같은 경우이다.</li>
	</ul>
	</li>
</ul>

<p>다음은 크기가 4×4인 체스판 위에 말이 4개 있는 경우이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/0aec7e3d-e8f5-428a-bebc-6a0fd514b387/-/preview/" style="width: 250px; height: 251px;"></p>

<p>첫 번째 턴은 다음과 같이 진행된다.</p>

<div class="table-responsive">
<table class="table table-bordered" style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 25%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/46796304-b486-4420-9d2c-ea49e2d5665b/-/preview/" style="width: 250px; height: 251px;"></td>
			<td style="width: 25%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/04643ced-fdfd-46f5-a07e-374704dbb1c5/-/preview/" style="width: 250px; height: 252px;"></td>
			<td style="width: 25%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/46f4bfab-841b-41c8-842e-56027816f846/-/preview/" style="width: 250px; height: 251px;"></td>
			<td style="width: 25%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/fcccf76c-9431-4ff5-8a05-7dbd2feff142/-/preview/" style="width: 250px; height: 251px;"></td>
		</tr>
	</tbody>
</table>
</div>

<p>두 번째 턴은 다음과 같이 진행된다.</p>

<div class="table-responsive">
<table class="table table-bordered" style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 25%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/36568153-8c2a-4fe9-b45f-72036c97f5aa/-/preview/" style="width: 250px; height: 252px;"></td>
			<td style="width: 25%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/babead43-4acc-425d-917a-54dcc6f45414/-/preview/" style="width: 250px; height: 251px;"></td>
			<td style="width: 25%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/1edd5ed8-0f4c-4c6d-b304-3b7642f42c6f/-/preview/" style="width: 250px; height: 251px;"></td>
			<td style="width: 25%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/028a5dd2-5524-4475-8439-9e7794e28ee4/-/preview/" style="width: 250px; height: 252px;"></td>
		</tr>
	</tbody>
</table>
</div>

<p>체스판의 크기와 말의 위치, 이동 방향이 모두 주어졌을 때, 게임이 종료되는 턴의 번호를 구해보자.</p>

<br>
<br>

### [Gold II] [원판 돌리기](https://www.acmicpc.net/problem/17822) - 17822 

<p>반지름이 1, 2, ..., N인 원판이 크기가 작아지는 순으로 바닥에 놓여있고, 원판의 중심은 모두 같다. 원판의 반지름이 i이면, 그 원판을 i번째 원판이라고 한다. 각각의 원판에는 M개의 정수가 적혀있고, i번째 원판에 적힌 j번째 수의 위치는 (i, j)로 표현한다. 수의 위치는 다음을 만족한다.</p>

<ul>
	<li>(i, 1)은 (i, 2), (i, M)과 인접하다.</li>
	<li>(i, M)은 (i, M-1), (i, 1)과 인접하다.</li>
	<li>(i, j)는 (i, j-1), (i, j+1)과 인접하다. (2 ≤ j ≤ M-1)</li>
	<li>(1, j)는 (2, j)와 인접하다.</li>
	<li>(N, j)는 (N-1, j)와 인접하다.</li>
	<li>(i, j)는 (i-1, j), (i+1, j)와 인접하다. (2 ≤ i ≤ N-1)</li>
</ul>

<p>아래 그림은 N = 3, M = 4인 경우이다.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 300px; height: 295px;"></p>

<p>원판의 회전은 독립적으로 이루어진다. 2번 원판을 회전했을 때, 나머지 원판은 회전하지 않는다. 원판을 회전시킬 때는 수의 위치를 기준으로 하며, 회전시킨 후의 수의 위치는 회전시키기 전과 일치해야 한다.</p>

<p>다음 그림은 원판을 회전시킨 예시이다.</p>

<div class="table-responsive">
<table class="table table-bordered" style="width:100%;">
	<tbody>
		<tr>
			<td style="width: 33%; text-align: center;"><img alt="" src="" style="width: 300px; height: 295px;"></td>
			<td style="width: 34%; text-align: center;"><img alt="" src="" style="width: 300px; height: 295px;"></td>
			<td style="width: 33%; text-align: center;"><img alt="" src="" style="width: 300px; height: 295px;"></td>
		</tr>
		<tr>
			<td style="width: 33%; text-align: center;">1번 원판을 시계 방향으로 1칸 회전</td>
			<td style="width: 34%; text-align: center;">2, 3번 원판을 반시계 방향으로 3칸 회전</td>
			<td style="width: 33%; text-align: center;">1, 3번 원판을 시계 방향으로 2칸 회전</td>
		</tr>
	</tbody>
</table>
</div>

<p>원판을 아래와 같은 방법으로 총 T번 회전시키려고 한다. 원판의 회전 방법은 미리 정해져 있고, i번째 회전할때 사용하는 변수는 x<sub>i</sub>, d<sub>i</sub>, k<sub>i</sub>이다.</p>

<ol>
	<li>번호가 x<sub>i</sub>의 배수인 원판을 d<sub>i</sub>방향으로 k<sub>i</sub>칸 회전시킨다. d<sub>i</sub>가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.</li>
	<li>원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
	<ol>
		<li>그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.</li>
		<li>없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.</li>
	</ol>
	</li>
</ol>

<p>원판을 T번 회전시킨 후 원판에 적힌 수의 합을 구해보자.</p>