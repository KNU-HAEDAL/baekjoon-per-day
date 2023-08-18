# 0817 - 구현

### [Silver II] [스타트와 링크](https://www.acmicpc.net/problem/14889) - 14889 

<p>오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.</p>

<p>BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 S<sub>ij</sub>는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 S<sub>ij</sub>의 합이다. S<sub>ij</sub>는 S<sub>ji</sub>와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 S<sub>ij</sub>와 S<sub>ji</sub>이다.</p>

<p>N=4이고, S가 아래와 같은 경우를 살펴보자.</p>

<table class="table table-bordered" style="width:20%">
	<thead>
		<tr>
			<th>i\j</th>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th>1</th>
			<td> </td>
			<td>1</td>
			<td>2</td>
			<td>3</td>
		</tr>
		<tr>
			<th>2</th>
			<td>4</td>
			<td> </td>
			<td>5</td>
			<td>6</td>
		</tr>
		<tr>
			<th>3</th>
			<td>7</td>
			<td>1</td>
			<td> </td>
			<td>2</td>
		</tr>
		<tr>
			<th>4</th>
			<td>3</td>
			<td>4</td>
			<td>5</td>
			<td> </td>
		</tr>
	</tbody>
</table>

<p>예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.</p>

<ul>
	<li>스타트 팀: S<sub>12</sub> + S<sub>21</sub> = 1 + 4 = 5</li>
	<li>링크 팀: S<sub>34</sub> + S<sub>43</sub> = 2 + 5 = 7</li>
</ul>

<p>1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.</p>

<ul>
	<li>스타트 팀: S<sub>13</sub> + S<sub>31</sub> = 2 + 7 = 9</li>
	<li>링크 팀: S<sub>24</sub> + S<sub>42</sub> = 6 + 4 = 10</li>
</ul>

<p>축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.</p>

### 풀이

<br>
<br>

### [Gold V] [톱니바퀴](https://www.acmicpc.net/problem/14891) - 14891 

<p>총 8개의 톱니를 가지고 있는 톱니바퀴 4개가 아래 그림과 같이 일렬로 놓여져 있다. 또, 톱니는 N극 또는 S극 중 하나를 나타내고 있다. 톱니바퀴에는 번호가 매겨져 있는데, 가장 왼쪽 톱니바퀴가 1번, 그 오른쪽은 2번, 그 오른쪽은 3번, 가장 오른쪽 톱니바퀴는 4번이다.</p>

<p>이때, 톱니바퀴를 총 K번 회전시키려고 한다. 톱니바퀴의 회전은 한 칸을 기준으로 한다. 회전은 시계 방향과 반시계 방향이 있고, 아래 그림과 같이 회전한다.</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14891/2.png" style="height:253px; width:660px"></p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14891/3.png" style="height:253px; width:602px"></p>

<p>톱니바퀴를 회전시키려면, 회전시킬 톱니바퀴와 회전시킬 방향을 결정해야 한다. 톱니바퀴가 회전할 때, 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수도 있고, 회전시키지 않을 수도 있다. 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된다.</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14891/4.png" style="height:223px; width:923px"></p>

<p>톱니바퀴의 초기 상태와 톱니바퀴를 회전시킨 방법이 주어졌을 때, 최종 톱니바퀴의 상태를 구하는 프로그램을 작성하시오.</p>

<br>
<br>

### [Gold IV] [감시](https://www.acmicpc.net/problem/15683) - 15683 

<p>스타트링크의 사무실은 1×1크기의 정사각형으로 나누어져 있는 N×M 크기의 직사각형으로 나타낼 수 있다. 사무실에는 총 K개의 CCTV가 설치되어져 있는데, CCTV는 5가지 종류가 있다. 각 CCTV가 감시할 수 있는 방법은 다음과 같다.</p>

<table class="table table table-bordered" style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 20%; text-align: center; vertical-align: middle;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15683/1.png" style="width: 113px; height: 70px;"></td>
			<td style="width: 20%; text-align: center;vertical-align: middle;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15683/2.png" style="width: 156px; height: 70px;"></td>
			<td style="width: 20%; text-align: center;vertical-align: middle;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15683/3.png" style="width: 100px; height: 100px;"></td>
			<td style="width: 20%; text-align: center;vertical-align: middle;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15683/4.png" style="width: 138px; height: 100px;"></td>
			<td style="width: 20%; text-align: center;vertical-align: middle;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15683/5.png" style="width: 149px; height: 150px;"></td>
		</tr>
		<tr>
			<td style="width: 20%; text-align: center;">1번</td>
			<td style="width: 20%; text-align: center;">2번</td>
			<td style="width: 20%; text-align: center;">3번</td>
			<td style="width: 20%; text-align: center;">4번</td>
			<td style="width: 20%; text-align: center;">5번</td>
		</tr>
	</tbody>
</table>

<p>1번 CCTV는 한 쪽 방향만 감시할 수 있다. 2번과 3번은 두 방향을 감시할 수 있는데, 2번은 감시하는 방향이 서로 반대방향이어야 하고, 3번은 직각 방향이어야 한다. 4번은 세 방향, 5번은 네 방향을 감시할 수 있다.</p>

<p>CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다. 사무실에는 벽이 있는데, CCTV는 벽을 통과할 수 없다. CCTV가 감시할 수 없는 영역은 사각지대라고 한다.</p>

<p>CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 하며, 감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.</p>

<p>지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호이다.</p>

<p>사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때, CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램을 작성하시오.</p>