# 0823 - 완전탐색(DFS), 구현

### [Gold II] [청소년 상어](https://www.acmicpc.net/problem/19236) - 19236 


<p><a href="/problem/16236">아기 상어</a>가 성장해 청소년 상어가 되었다.</p>

<p>4×4크기의 공간이 있고, 크기가 1×1인 정사각형 칸으로 나누어져 있다. 공간의 각 칸은 (x, y)와 같이 표현하며, x는 행의 번호, y는 열의 번호이다. 한 칸에는 물고기가 한 마리 존재한다. 각 물고기는 번호와 방향을 가지고 있다. 번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수이며, 두 물고기가 같은 번호를 갖는 경우는 없다. 방향은 8가지 방향(상하좌우, 대각선) 중 하나이다.</p>

<p>오늘은 청소년 상어가 이 공간에 들어가 물고기를 먹으려고 한다. 청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다. 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 이후 물고기가 이동한다.</p>

<p>물고기는 번호가 작은 물고기부터 순서대로 이동한다. 물고기는 한 칸을 이동할 수 있고, 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸, 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다. 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다. 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다. 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.</p>

<p>물고기의 이동이 모두 끝나면 상어가 이동한다. 상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다. 상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다. 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다. 물고기가 없는 칸으로는 이동할 수 없다. 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다. 상어가 이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복된다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/1c7c473e-5e2c-4c45-9c88-b3b7cd06a360/-/preview/" style="width: 333px; height: 338px;"></p>

<p style="text-align: center;"><그림 1></p>

<p><그림 1>은 청소년 상어가 공간에 들어가기 전 초기 상태이다. 상어가 공간에 들어가면 (0, 0)에 있는 7번 물고기를 먹고, 상어의 방향은 ↘이 된다. <그림 2>는 상어가 들어간 직후의 상태를 나타낸다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/8f26df12-6f68-43a3-9f6e-7416144e91dc/-/preview/" style="width: 328px; height: 332px;"></p>

<p style="text-align: center;"><그림 2></p>

<p>이제 물고기가 이동해야 한다. 1번 물고기의 방향은 ↗이다. ↗ 방향에는 칸이 있고, 15번 물고기가 들어있다. 물고기가 있는 칸으로 이동할 때는 그 칸에 있는 물고기와 위치를 서로 바꿔야 한다. 따라서, 1번 물고기가 이동을 마치면 <그림 3>과 같아진다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/75315b3c-ee04-4ae8-9422-5b1137f86117/-/preview/" style="width: 326px; height: 331px;"></p>

<p style="text-align: center;"><그림 3></p>

<p>2번 물고기의 방향은 ←인데, 그 방향에는 상어가 있으니 이동할 수 없다. 방향을 45도 반시계 회전을 하면 ↙가 되고, 이 칸에는 3번 물고기가 있다. 물고기가 있는 칸이니 서로 위치를 바꾸고, <그림 4>와 같아지게 된다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/7be317c7-b8b5-4b83-becb-ffd8550311fb/-/preview/" style="width: 327px; height: 329px;"></p>

<p style="text-align: center;"><그림 4></p>

<p>3번 물고기의 방향은 ↑이고, 존재하지 않는 칸이다. 45도 반시계 회전을 한 방향 ↖도 존재하지 않으니, 다시 회전을 한다. ← 방향에는 상어가 있으니 또 회전을 해야 한다. ↙ 방향에는 2번 물고기가 있으니 서로의 위치를 교환하면 된다. 이런 식으로 모든 물고기가 이동하면 <그림 5>와 같아진다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/a58fbda0-bb64-4773-b5f9-2da0bd3f0fd2/-/preview/" style="width: 330px; height: 329px;"></p>

<p style="text-align: center;"><그림 5></p>

<p>물고기가 모두 이동했으니 이제 상어가 이동할 순서이다. 상어의 방향은 ↘이고, 이동할 수 있는 칸은 12번 물고기가 있는 칸, 15번 물고기가 있는 칸, 8번 물고기가 있는 칸 중에 하나이다. 만약, 8번 물고기가 있는 칸으로 이동하면, <그림 6>과 같아지게 된다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/2431d117-fab6-4de9-8d76-2fb41d471ee7/-/crop/651x656/1,12/-/preview/" style="width: 326px; height: 328px;"></p>

<p style="text-align: center;"><그림 6></p>

<p>상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구해보자.</p>

<br>
<br>

### [Gold II] [어른 상어](https://www.acmicpc.net/problem/19237) - 19237  

<p><a href="/problem/19236">청소년 상어</a>는 더욱 자라 어른 상어가 되었다. 상어가 사는 공간에 더 이상 물고기는 오지 않고 다른 상어들만이 남아있다. 상어에는 1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다. 상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데, 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.</p>

<p>N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다. 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다. 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다. 냄새는 상어가 k번 이동하고 나면 사라진다.</p>

<p>각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다. 우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다. 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.</p>

<p>모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/149aa507-f474-43cb-9071-1959bb83d59a/-/preview/" style="width: 353px; height: 352px;"></p>

<p style="text-align: center;"><그림 1></p>

<table class="table table-border table table-bordered" style="width: 100%;">
	<thead>
		<tr>
			<th colspan="8" style="text-align: center;">우선 순위</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th colspan="2" style="text-align: center;">상어 1</th>
			<th colspan="2" style="text-align: center;">상어 2</th>
			<th colspan="2" style="text-align: center;">상어 3</th>
			<th colspan="2" style="text-align: center;">상어 4</th>
		</tr>
		<tr>
			<th style="text-align: center;">↑</th>
			<td style="text-align: center;">↓ ← ↑ →</td>
			<th style="text-align: center;">↑</th>
			<td style="text-align: center;">↓ → ← ↑</td>
			<th style="text-align: center;">↑</th>
			<td style="text-align: center;">→ ← ↓ ↑</td>
			<th style="text-align: center;">↑</th>
			<td style="text-align: center;">← → ↑ ↓</td>
		</tr>
		<tr>
			<th style="text-align: center;">↓</th>
			<td style="text-align: center;">→ ↑ ↓ ←</td>
			<th style="text-align: center;">↓</th>
			<td style="text-align: center;">↓ ↑ ← →</td>
			<th style="text-align: center;">↓</th>
			<td style="text-align: center;">↑ → ← ↓</td>
			<th style="text-align: center;">↓</th>
			<td style="text-align: center;">← ↓ → ↑</td>
		</tr>
		<tr>
			<th style="text-align: center;">←</th>
			<td style="text-align: center;">← → ↓ ↑</td>
			<th style="text-align: center;">←</th>
			<td style="text-align: center;">← → ↑ ↓</td>
			<th style="text-align: center;">←</th>
			<td style="text-align: center;">↑ ← ↓ →</td>
			<th style="text-align: center;">←</th>
			<td style="text-align: center;">↑ → ↓ ←</td>
		</tr>
		<tr>
			<th style="text-align: center;">→</th>
			<td style="text-align: center;">→ ← ↑ ↓</td>
			<th style="text-align: center;">→</th>
			<td style="text-align: center;">→ ↑ ↓ ←</td>
			<th style="text-align: center;">→</th>
			<td style="text-align: center;">← ↓ ↑ →</td>
			<th style="text-align: center;">→</th>
			<td style="text-align: center;">↑ → ↓ ←</td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><표 1></p>

<p><그림 1>은 맨 처음에 모든 상어가 자신의 냄새를 뿌린 상태를 나타내며, <표 1>에는 각 상어 및 현재 방향에 따른 우선순위가 표시되어 있다. 이 예제에서는 k = 4이다. 왼쪽 하단에 적힌 정수는 냄새를 의미하고, 그 값은 사라지기까지 남은 시간이다. 좌측 상단에 적힌 정수는 상어의 번호 또는 냄새를 뿌린 상어의 번호를 의미한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/b2d80580-57ba-419b-9d16-bc7fbe49512b/-/preview/" style="width: 900px; height: 352px;"></p>

<p style="text-align: center;"><그림 2></p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/52324aeb-3f7d-49b0-8128-560eb3742aa3/-/preview/" style="width: 901px; height: 358px;"></p>

<p style="text-align: center;"><그림 3></p>

<p><그림 2>는 모든 상어가 한 칸 이동하고 자신의 냄새를 뿌린 상태이고, <그림 3>은 <그림 2>의 상태에서 한 칸 더 이동한 것이다. (2, 4)에는 상어 2과 4가 같이 도달했기 때문에, 상어 4는 격자 밖으로 쫓겨났다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/86821cd6-b638-43a1-8abb-99c917d6d324/-/preview/" style="width: 901px; height: 355px;"></p>

<p style="text-align: center;"><그림 4></p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/76e735b6-44e1-437c-9b69-b7f55ea29d02/-/preview/" style="width: 902px; height: 357px;"></p>

<p style="text-align: center;"><그림 5></p>

<p><그림 4>은 격자에 남아있는 모든 상어가 한 칸 이동하고 자신의 냄새를 뿌린 상태, <그림 5>는 <그림 4>에서 한 칸 더 이동한 상태를 나타낸다. 상어 2는 인접한 칸 중에 아무 냄새도 없는 칸이 없으므로 자신의 냄새가 들어있는 (2, 4)으로 이동했다. 상어가 이동한 후에, 맨 처음에 각 상어가 뿌린 냄새는 사라졌다.</p>

<p>이 과정을 반복할 때, 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지를 구하는 프로그램을 작성하시오.</p>