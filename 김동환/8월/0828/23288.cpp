#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, m, k;
int board[21][21];
int dy[] = {0, 1, 0, -1}, dx[] = {1, 0, -1, 0};

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < m;
}

pair<int, int> rotateDice(int upNum, int rightNum, int dir) {
  int adjacentNum[7][4] = {
    {0, 0, 0, 0},
    {3, 5, 4, 2},
    {3, 1, 4, 6},
    {6, 5, 1, 2},
    {1, 5, 6, 2},
    {3, 6, 4, 1},
    {3, 2, 4, 5}
  };

  int diffDir;
  for(int i = 0; i < 4; i++) {
    if (adjacentNum[upNum][i] == rightNum) {
      diffDir = i;
      break;
    }
  }

  int nextUpNum = adjacentNum[upNum][(diffDir + dir + 2) % 4];

  int nextRightNum;
  if (dir == 0) {
    nextRightNum = upNum;
  }
  else if (dir == 2) {
    for(int i = 0; i < 4; i++) {
      if (adjacentNum[nextUpNum][i] == upNum) {
          nextRightNum = adjacentNum[nextUpNum][(i + 2) % 4];
          break;
      }
    }
  }
  else {
    nextRightNum = rightNum;
  }

  return make_pair(nextUpNum, nextRightNum);
}

int getScore(int sy, int sx) {
  int curNum = board[sy][sx];

  queue<pair<int, int>> q;
  bool visited[21][21] = {false};

  q.push({sy, sx});
  visited[sy][sx] = true;

  int count = 0;
  while(not q.empty()) {
    int y = q.front().first;
    int x = q.front().second;
    q.pop();

    count++;

    for(int i = 0; i < 4; i++) {
      int ny = y + dy[i];
      int nx = x + dx[i];

      if (isInside(ny, nx) and board[ny][nx] == curNum and not visited[ny][nx]) {
        q.push({ny, nx});
        visited[ny][nx] = true;
      }
    }
  }

  return count * curNum;
}

int getBottomNum(int upNum) {
  return 7 - upNum;
}

int solve() {
  int y = 0, x = 0, dir = 0;
  int upNum = 1, rightNum = 3;
  int score = 0;

  while(k--) {
    // 주사위 굴리기 - 칸 이동
    int ny = y + dy[dir];
    int nx = x + dx[dir];
    if (not isInside(ny, nx)) {
      dir = (dir + 2) % 4;

      ny = y + dy[dir];
      nx = x + dx[dir];
    }

    y = ny;
    x = nx;

    // 주사위 굴리기 - 주사위 회전 구현
    pair<int, int> rotateResult = rotateDice(upNum, rightNum, dir);
    upNum = rotateResult.first;
    rightNum = rotateResult.second;

    // 점수 더하기
    score += getScore(y, x);

    // 다음 이동 방향 결정
    int bottomNum = getBottomNum(upNum);
    if (bottomNum > board[y][x]) {
      dir = (dir + 1) % 4;
    }
    else if (bottomNum < board[y][x]) {
      dir = (dir + 3) % 4;
    }
  }

  return score;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n >> m >> k;

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      cin >> board[i][j];
    }
  }

  cout << solve() << endl;

  return 0;
}
