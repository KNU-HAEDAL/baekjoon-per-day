# 0822 - 완전탐색(백트래킹), 구현
 
### [Gold II] [주사위 윷놀이](https://www.acmicpc.net/problem/17825) - 17825 

<p>주사위 윷놀이는 다음과 같은 게임판에서 하는 게임이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/43409ac6-54bf-4a21-b542-e01a8211e59f/-/preview/" style="width: 640px; height: 585px;"></p>

<ul>
	<li>처음에는 시작 칸에 말 4개가 있다.</li>
	<li>말은 게임판에 그려진 화살표의 방향대로만 이동할 수 있다. 말이 파란색 칸에서 이동을 시작하면 파란색 화살표를 타야 하고, 이동하는 도중이거나 파란색이 아닌 칸에서 이동을 시작하면 빨간색 화살표를 타야 한다. 말이 도착 칸으로 이동하면 주사위에 나온 수와 관계 없이 이동을 마친다.</li>
	<li>게임은 10개의 턴으로 이루어진다. 매 턴마다 1부터 5까지 한 면에 하나씩 적혀있는 5면체 주사위를 굴리고, 도착 칸에 있지 않은 말을 하나 골라 주사위에 나온 수만큼 이동시킨다.</li>
	<li>말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다. 단, 이동을 마치는 칸이 도착 칸이면 고를 수 있다.</li>
	<li>말이 이동을 마칠 때마다 칸에 적혀있는 수가 점수에 추가된다.</li>
</ul>

<p>주사위에서 나올 수 10개를 미리 알고 있을 때, 얻을 수 있는 점수의 최댓값을 구해보자.</p>

<br>
<br>

### [Gold II] [모노미노도미노 2](https://www.acmicpc.net/problem/20061) - 20061 

<p>모노미노도미노는 아래와 같이 생긴 보드에서 진행되는 게임이다. 보드는 빨간색 보드, 파란색 보드, 초록색 보드가 그림과 같이 붙어있는 형태이다. 게임에서 사용하는 좌표 (x, y)에서 x는 행, y는 열을 의미한다. 빨간색, 파란색, 초록색 보드가 사용하는 좌표는 그 색으로 그림에 적혀있다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/8043086d-a85c-4d9e-8505-7a4ffd8c4439/-/preview/" style="width: 611px; height: 624px;"></p>

<p style="text-align: center;"><그림 1> 모노미노도미노 게임 보드</p>

<p>이 게임에서 사용하는 블록은 타일 하나 또는 두 개가 가로 또는 세로로 붙어있는 형태이다. 아래와 같이 세 종류가 있으며, 왼쪽부터 순서대로 크기가 1×1, 1×2, 2×1 이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/1453b25c-e0c1-4b99-9eda-bba9336beab1/-/preview/" style="width: 335px; height: 129px;"></p>

<p style="text-align: center;"><그림 2> 모노미노도미노 게임에서 사용하는 블록</p>

<p>블록을 놓을 위치를 빨간색 보드에서 선택하면, 그 위치부터 초록색 보드로 블록이 이동하고, 파란색 보드로 블록이 이동한다. 블록의 이동은 다른 블록을 만나거나 보드의 경계를 만나기 전까지 계속해서 이동한다. 예를 들어, 크기가 1×1인 블록을 (1, 1)에 놓으면, 보드의 상태는 <그림 3>과 같이 변한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/49d72bb4-859c-422f-845b-00e6699023b7/-/preview/" style="width: 623px; height: 627px;"></p>

<p style="text-align: center;"><그림 3></p>

<p>여기서 크기가 1×2인 블록을 (3, 0)과 (3, 1)에 놓으면 <그림 4>와 같이 보드의 상태가 변한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/4fc4574a-3e42-42ab-991f-3417104239a5/-/preview/" style="width: 608px; height: 617px;"></p>

<p style="text-align: center;"><그림 4></p>

<p>다시 이 상태에서 크기가 2×1인 블록을 (2, 2), (3, 2)와 (2, 3), (3, 3)에 놓으면 <그림 5>와 같이 변한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/d6f4303f-06e7-4918-8cb4-da0356a6b5c6/-/preview/" style="width: 609px; height: 615px;"></p>

<p style="text-align: center;"><그림 5></p>

<p>초록색 보드의 4번 행은 모든 칸이 타일로 가득 차있다. 이렇게 초록색 보드에서 어떤 행이 타일로 가득 차 있다면, 그 행의 타일은 모두 사라진다. 사라진 이후에는 초록색 보드에서 사라진 행의 위에 있는 블록이 사라진 행의 수만큼 아래로 이동한다. 파란색의 경우는 열이 타일로 가득 차 있으면, 그 열의 타일이 모두 사라지며, 사라진 이후에는 파란색 보드에서 사라진 열의 왼쪽에 있는 블록이 사라진 열의 수만큼 오른쪽으로 이동한다. 이렇게 한 행이나 열이 타일로 가득 차서 사라지면 1점을 획득한다. 점수는 사라진 행 또는 열의 수와 같다. 만약, 두 개의 행이 사라지면 2점을 획득하게 되고, 한 행과 한 열이 사라져도 2점을 획득하게 된다. 위의 보드는 아래와 같이 변하고, 1점을 얻는다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/106542a6-ee12-4d30-9000-f78fb96c8908/-/preview/" style="width: 606px; height: 615px;"></p>

<p style="text-align: center;"><그림 6></p>

<p>여기서 크기가 2×1인 블록을 (1, 3), (2, 3)에 놓으면 보드는 <그림 7>과 같이 변한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/911438b0-7b7f-43b8-b6cc-20c6390bc7e3/-/preview/" style="width: 614px; height: 614px;"></p>

<p style="text-align: center;"><그림 7></p>

<p>초록색 보드의 0, 1번 행과 파란색 보드의 0, 1번 열은 그림에는 연한색으로 표현되어 있는 특별한 칸이다. 초록색 보드의 0, 1번 행에 블록이 있으면, 블록이 있는 행의 수만큼 아래 행에 있는 타일이 사라지고, 초록색 보드의 모든 블록이 사라진 행의 수만큼 아래로 이동하고, 파란색 보드의 0, 1번 열에 블록이 있으면, 블록이 있는 열의 수만큼 오른쪽 열에 있는 타일이 사라지고, 파란색 보드의 모든 블록이 사라진 열의 수만큼 이동하게 된다. 위의 그림은 파란색 보드의 1번 열에 블록이 있기 때문에, 5번 열에 있는 블록이 모두 사라지고, 파란색 보드의 모든 블록이 오른쪽으로 한 칸 이동하게 된다. 따라서, 보드는 <그림 8>과 같이 변하게 된다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/9b59b0ff-ebfc-4283-9576-5bec2bf2f238/-/preview/" style="width: 615px; height: 615px;"></p>

<p style="text-align: center;"><그림 8></p>

<p>위의 보드에서 1×2인 블록을 (0, 0), (0, 1)에 놓으면 <그림 9>와 같다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/c2151fd5-4e43-4403-bf10-7cbef642a6eb/-/preview/" style="width: 608px; height: 614px;"></p>

<p style="text-align: center;"><그림 9></p>

<p>여기서 크기가 2×1인 블록을 (2, 0), (3, 0)에 놓으면 <그림 10>과 같이 변한다. 파란색 보드는 1번 열에 블록이 생겨서 오른쪽으로 한 칸씩 이동한 상태이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/0fd074f1-72af-4ffe-95d0-038635b7a80c/-/preview/" style="width: 611px; height: 618px;"></p>

<p style="text-align: center;"><그림 10></p>

<p>크기가 2×1인 블록을 (1, 2), (2, 2)에 놓으면, <그림 11>과 같이 변한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/f5941153-b92d-42ef-b25c-453e600f884c/-/preview/" style="width: 601px; height: 612px;"></p>

<p style="text-align: center;"><그림 11></p>

<p>파란색 보드는 1번 열에 블록이 있기 때문에, 5번 열의 타일이 사라지고 모든 블록이 오른쪽으로 한 칸씩 이동하게 된다. 초록색 보드는 4번 행의 모든 칸에 타일이 있기 때문에, 1점을 얻으면서, 4번 행의 모든 타일이 사라진다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/1153c233-befa-477d-a385-a10be375ff50/-/preview/" style="width: 609px; height: 616px;"></p>

<p style="text-align: center;"><그림 12></p>

<p><그림 12>는 <그림 11>의 상태에서 파란색 보드는 모든 블록이 오른쪽으로 한 칸 이동했고, 초록색 보드의 4번 행이 모두 사라진 상태이다. 이제, 초록색 보드에서 사라진 행의 위에 있는 블록이 아래로 한 칸씩 내려와야 한다. 이동한 후의 상태는 <그림 13>과 같다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/81a0a734-129b-47e8-8142-5579f747f678/-/preview/" style="width: 609px; height: 618px;"></p>

<p style="text-align: center;"><그림 13></p>

<p>행이나 열이 타일로 가득찬 경우와 연한 칸에 블록이 있는 경우가 동시에 발생할 수 있다. 이 경우에는 행이나 열이 타일로 가득 찬 경우가 없을 때까지 점수를 획득하는 과정이 모두 진행된 후, 연한 칸에 블록이 있는 경우를 처리해야 한다.</p>

<p>블록은 보드에 놓인 이후에 다른 블록과 합쳐지지 않는다. 블록을 놓은 위치가 순서대로 주어졌을 때, 얻은 점수와 초록색 보드와 파란색 보드에 타일이 있는 칸의 개수를 모두 구해보자.</p>