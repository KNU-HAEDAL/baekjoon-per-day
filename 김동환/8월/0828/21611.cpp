#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, m;
int board[51][51];
int result = 0;
int dy[] = {-1, 1, 0, 0}, dx[] = {0, 0, -1, 1};
vector<pair<int, int>> line;

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < n;
}

void initLine() {
  int y = n / 2, x = n / 2;
  int dyForFunc[] = {0, 1, 0, -1}, dxForFunc[] = {-1, 0, 1, 0};
  int dist = 1, dir = 0;

  while(true) {
    for(int i = 0; i < dist; i++) {
      y += dyForFunc[dir];
      x += dxForFunc[dir];

      if (x == -1) {
        return;
      }

      line.push_back({y, x});
    }

    dir = (dir + 1) % 4;

    for(int i = 0; i < dist; i++) {
      y += dyForFunc[dir];
      x += dxForFunc[dir];

      line.push_back({y, x});
    }

    dir = (dir + 1) % 4;
    dist++;
  }
}

void blizzard(int dir, int speed) {
  int y = n / 2, x = n / 2;

  for(int i = 0; i < speed; i++) {
    y += dy[dir];
    x += dx[dir];

    if (not isInside(y, x)) {
      break;
    }

    board[y][x] = 0;
  }
}

void moveBall() {
  for(int i = 1; i < line.size(); i++) {
    for(int j = i; j > 0; j--) {
      int prevY = line[j - 1].first;
      int prevX = line[j - 1].second;
      int y = line[j].first;
      int x = line[j].second;

      if (board[y][x] > 0 and board[prevY][prevX] == 0) {
        board[prevY][prevX] = board[y][x];
        board[y][x] = 0;
      }
      else {
        break;
      }
    }
  }
}

int getGroupSize(int pos) {
  int y = line[pos].first;
  int x = line[pos].second;
  int curColor = board[y][x];
  int sameCount = 1;

  if (curColor == 0) {
    return sameCount;
  }

  for(int i = pos + 1; i < line.size(); i++) {
    int ny = line[i].first;
    int nx = line[i].second;
    int nColor = board[ny][nx];

    if (curColor == nColor) {
      sameCount++;
    }
    else {
      break;
    }
  }

  return sameCount;
}

int explodeBall() {
  int score = 0;

  int lineSize = line.size();
  for(int i = 0; i < lineSize;) {
    int y = line[i].first;
    int x = line[i].second;
    int color = board[y][x];

    int groupSize = getGroupSize(i);

    if (groupSize >= 4) {
      score += color * groupSize;

      for(int j = i; j < i + groupSize; j++) {
        int ty = line[j].first;
        int tx = line[j].second;

        board[ty][tx] = 0;
      }
    }

    i += groupSize;
  }

  return score;
}

void transformBall() {
  vector<int> transformedBalls;
  for(int i = 0; i < line.size();) {
    int y = line[i].first;
    int x = line[i].second;
    int color = board[y][x];

    if (color == 0) {
      break;
    }

    int groupSize = getGroupSize(i);

    transformedBalls.push_back(groupSize);
    transformedBalls.push_back(color);

    i += groupSize;
  }

  for(int i = 0; i < line.size() and i < transformedBalls.size(); i++) {
    int y = line[i].first;
    int x = line[i].second;
    int color = transformedBalls[i];

    board[y][x] = color;
  }
}

int solve() {
  initLine();

  int result = 0;
  while(m--) {
    int speed, dir;
    cin >> dir >> speed;

    // 블리자드 마법
    blizzard(dir - 1, speed);

    int score = 0;
    do {
      // 구슬 이동
      moveBall();

      // 구슬 폭발
      score = explodeBall();

      result += score;
    } while(score > 0);

    transformBall();
  }

  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n >> m;

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      cin >> board[i][j];
    }
  }

  cout << solve() << endl;

  return 0;
}
