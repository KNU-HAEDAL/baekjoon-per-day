# 0828 - 완전탐색(BFS), 구현

### [Gold II] [상어 중학교](https://www.acmicpc.net/problem/21609) - 21609 

<p>상어 중학교의 코딩 동아리에서 게임을 만들었다. 이 게임은 크기가 N×N인 격자에서 진행되고, 초기에 격자의 모든 칸에는 블록이 하나씩 들어있고, 블록은 검은색 블록, 무지개 블록, 일반 블록이 있다. 일반 블록은 M가지 색상이 있고, 색은 M이하의 자연수로 표현한다. 검은색 블록은 -1, 무지개 블록은 0으로 표현한다. (i, j)는 격자의 i번 행, j번 열을 의미하고, |r<sub>1</sub> - r<sub>2</sub>| + |c<sub>1</sub> - c<sub>2</sub>| = 1을 만족하는 두 칸 (r<sub>1</sub>, c<sub>1</sub>)과 (r<sub>2</sub>, c<sub>2</sub>)를 인접한 칸이라고 한다.</p>

<p>블록 그룹은 연결된 블록의 집합이다. 그룹에는 일반 블록이 적어도 하나 있어야 하며, 일반 블록의 색은 모두 같아야 한다. 검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다. 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며, 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다. 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.</p>

<p>오늘은 이 게임에 오토 플레이 기능을 만드려고 한다. 오토 플레이는 다음과 같은 과정이 블록 그룹이 존재하는 동안 계속해서 반복되어야 한다.</p>

<ol>
	<li>크기가 가장 큰 블록 그룹을 찾는다. 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.</li>
	<li>1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B<sup>2</sup>점을 획득한다.</li>
	<li>격자에 중력이 작용한다.</li>
	<li>격자가 90도 반시계 방향으로 회전한다.</li>
	<li>다시 격자에 중력이 작용한다.</li>
</ol>

<p>격자에 중력이 작용하면 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동한다. 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속 된다.</p>

<p>다음은 N = 5, M = 3인 경우의 예시이다.</p>

<table class="table table-bordered table-center-30 table-21609">
	<tbody>
		<tr>
			<td>2</td>
			<td>2</td>
			<td>-1</td>
			<td>3</td>
			<td>1</td>
		</tr>
		<tr>
			<td>3</td>
			<td>3</td>
			<td>2</td>
			<td>0</td>
			<td>-1</td>
		</tr>
		<tr>
			<td>0</td>
			<td>0</td>
			<td>0</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>-1</td>
			<td>3</td>
			<td>1</td>
			<td>3</td>
			<td>2</td>
		</tr>
		<tr>
			<td>0</td>
			<td>3</td>
			<td>2</td>
			<td>2</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<p>여기서 찾을 수 있는 크기가 가장 큰 블록 그룹을 다음과 같이 빨간색으로 표시했다.</p>

<table class="table table-bordered table-center-30 table-21609">
	<tbody>
		<tr>
			<td>2</td>
			<td>2</td>
			<td>-1</td>
			<td>3</td>
			<td>1</td>
		</tr>
		<tr>
			<td class="bg-red">3</td>
			<td class="bg-red">3</td>
			<td>2</td>
			<td>0</td>
			<td>-1</td>
		</tr>
		<tr>
			<td class="bg-red">0</td>
			<td class="bg-red">0</td>
			<td class="bg-red">0</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>-1</td>
			<td class="bg-red">3</td>
			<td>1</td>
			<td>3</td>
			<td>2</td>
		</tr>
		<tr>
			<td class="bg-red">0</td>
			<td class="bg-red">3</td>
			<td>2</td>
			<td>2</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<p>블록 그룹이 제거되면 다음과 같이 변하고, 점수 8<sup>2</sup>점을 획득한다.</p>

<table class="table table-bordered table-center-30 table-21609">
	<tbody>
		<tr>
			<td>2</td>
			<td>2</td>
			<td>-1</td>
			<td>3</td>
			<td>1</td>
		</tr>
		<tr>
			<td> </td>
			<td> </td>
			<td>2</td>
			<td>0</td>
			<td>-1</td>
		</tr>
		<tr>
			<td> </td>
			<td> </td>
			<td> </td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>-1</td>
			<td> </td>
			<td>1</td>
			<td>3</td>
			<td>2</td>
		</tr>
		<tr>
			<td> </td>
			<td> </td>
			<td>2</td>
			<td>2</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<p>중력이 작용하면 다음과 같이 변한다.</p>

<table class="table table-bordered table-center-30 table-21609">
	<tbody>
		<tr>
			<td> </td>
			<td> </td>
			<td>-1</td>
			<td>3</td>
			<td>1</td>
		</tr>
		<tr>
			<td> </td>
			<td> </td>
			<td> </td>
			<td>0</td>
			<td>-1</td>
		</tr>
		<tr>
			<td>2</td>
			<td> </td>
			<td>2</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>-1</td>
			<td> </td>
			<td>1</td>
			<td>3</td>
			<td>2</td>
		</tr>
		<tr>
			<td> </td>
			<td>2</td>
			<td>2</td>
			<td>2</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<p>90도 반시계방향으로 회전한 결과는 다음과 같다.</p>

<table class="table table-bordered table-center-30 table-21609">
	<tbody>
		<tr>
			<td>1</td>
			<td>-1</td>
			<td>2</td>
			<td>2</td>
			<td>1</td>
		</tr>
		<tr>
			<td>3</td>
			<td>0</td>
			<td>1</td>
			<td>3</td>
			<td>2</td>
		</tr>
		<tr>
			<td>-1</td>
			<td> </td>
			<td>2</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td>2</td>
		</tr>
		<tr>
			<td> </td>
			<td> </td>
			<td>2</td>
			<td>-1</td>
			<td> </td>
		</tr>
	</tbody>
</table>

<p>다시 여기서 중력이 작용하면 다음과 같이 변한다.</p>

<table class="table table-bordered table-center-30 table-21609">
	<tbody>
		<tr>
			<td>1</td>
			<td>-1</td>
			<td> </td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<td>3</td>
			<td> </td>
			<td>2</td>
			<td>2</td>
			<td>1</td>
		</tr>
		<tr>
			<td>-1</td>
			<td> </td>
			<td>1</td>
			<td>3</td>
			<td>2</td>
		</tr>
		<tr>
			<td> </td>
			<td> </td>
			<td>2</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td> </td>
			<td>0</td>
			<td>2</td>
			<td>-1</td>
			<td>2</td>
		</tr>
	</tbody>
</table>

<p>오토 플레이가 모두 끝났을 때 획득한 점수의 합을 구해보자.</p>
<br>
<br>

### [Gold V] [마법사 상어와 비바라기](https://www.acmicpc.net/problem/21610) - 21610  

<p>마법사 상어는 <a href="/problem/20056">파이어볼</a>, <a href="/problem/20057">토네이도</a>, <a href="/problem/20058">파이어스톰</a>, 물복사버그 마법을 할 수 있다. 오늘 새로 배운 마법은 비바라기이다. 비바라기를 시전하면 하늘에 비구름을 만들 수 있다. 오늘은 비바라기를 크기가 N×N인 격자에서 연습하려고 한다. 격자의 각 칸에는 바구니가 하나 있고, 바구니는 칸 전체를 차지한다. 바구니에 저장할 수 있는 물의 양에는 제한이 없다. (r, c)는 격자의 r행 c열에 있는 바구니를 의미하고, A[r][c]는 (r, c)에 있는 바구니에 저장되어 있는 물의 양을 의미한다.</p>

<p>격자의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)이다. 마법사 상어는 연습을 위해 1번 행과 N번 행을 연결했고, 1번 열과 N번 열도 연결했다. 즉, N번 행의 아래에는 1번 행이, 1번 행의 위에는 N번 행이 있고, 1번 열의 왼쪽에는 N번 열이, N번 열의 오른쪽에는 1번 열이 있다.</p>

<p>비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다. 구름은 칸 전체를 차지한다. 이제 구름에 이동을 M번 명령하려고 한다. i번째 이동 명령은 방향 d<sub>i</sub>과 거리 s<sub>i</sub>로 이루어져 있다. 방향은 총 8개의 방향이 있으며, 8개의 정수로 표현한다. 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 이다. 이동을 명령하면 다음이 순서대로 진행된다.</p>

<ol>
	<li>모든 구름이 d<sub>i</sub> 방향으로 s<sub>i</sub>칸 이동한다.</li>
	<li>각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.</li>
	<li>구름이 모두 사라진다.</li>
	<li>2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
	<ul>
		<li>이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.</li>
		<li>예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.</li>
	</ul>
	</li>
	<li>바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.</li>
</ol>

<p>M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.</p>