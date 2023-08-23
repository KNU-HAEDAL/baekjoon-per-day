#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


#define EMPTY -2
#define BLACK -1
#define RAINBOW 0

int n, m;
int board[21][21];
int dy[] = {-1, 0, 1, 0}, dx[] = {0, 1, 0, -1};

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < n;
}

pair<int, int> bfs(int sy, int sx, bool normalBlockVisited[21][21]) {
  queue<pair<int, int>> q;
  bool visited[21][21] = {false};

  q.push({sy, sx});
  visited[sy][sx] = true;
  normalBlockVisited[sy][sx] = true;
  int targetBlock = board[sy][sx];
  int sizeOfGroup = 1, countOfRainbow = 0;

  while(not q.empty()) {
    int y = q.front().first;
    int x = q.front().second;
    q.pop();

    for(int i = 0; i < 4; i++) {
      int ny = y + dy[i];
      int nx = x + dx[i];

      if (isInside(ny, nx) and not visited[ny][nx]) {
        if (board[ny][nx] == targetBlock or board[ny][nx] == RAINBOW) {
          q.push({ny, nx});
          visited[ny][nx] = true;
          normalBlockVisited[ny][nx] = true;
          sizeOfGroup++;

          if (board[ny][nx] == RAINBOW) {
            countOfRainbow++;
          }
        }
      }
    }
  }

  return make_pair(sizeOfGroup, countOfRainbow);
}

vector<pair<pair<int, int>, pair<int, int>>> makeGroup() {
  vector<pair<pair<int, int>, pair<int, int>>> groups;
  bool visited[21][21] = { false };

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      if (board[i][j] > RAINBOW and not visited[i][j]) {
        pair<int, int> info = bfs(i, j, visited);

        groups.push_back({{i, j}, info});
      }
    }
  }

  return groups;
}

bool compare(pair<pair<int, int>, pair<int, int>> a, pair<pair<int, int>, pair<int, int>> b) {
  if (a.second.first != b.second.first) {
    return a.second.first > b.second.first;
  }
  if (a.second.second != b.second.second) {
    return a.second.second > b.second.second;
  }
  if (a.first.first != b.first.first) {
    return a.first.first > b.first.first;
  }
  return a.first.second > b.first.second;
}

int removeGroup(pair<int, int> groupPos) {
  bool visited[21][21] = {false};

  pair<int, int> info = bfs(groupPos.first, groupPos.second, visited);
  int gainedScore = info.first * info.first;

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      if (visited[i][j]) {
        board[i][j] = EMPTY;
      }
    }
  }

  return gainedScore;
}

void applyGravity() {
  for(int x = 0; x < n; x++) {
    for(int y = n - 2; y >= 0; y--) {
      if (board[y][x] <= BLACK) {
        continue;
      }

      // board[y][x]에 있는 블럭에 중력을 적용할 것임.
      // 이는 가장자리(board[n - 1][x])까지 도달하거나 다른 블럭을 만날 때까지 반복
      for(int i = y + 1; i < n; i++) {
        if (board[i][x] == EMPTY) {
          board[i][x] = board[i - 1][x];
          board[i - 1][x] = EMPTY;
        }
        else {
          break;
        }
      }
    }
  }
}

void rotate() {
  int tmp[21][21] = { 0 };
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      tmp[n - j - 1][i] = board[i][j];
    }
  }

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      board[i][j] = tmp[i][j];
    }
  }
}

int solve() {
  int score = 0;

  while(true) {
    // bfs 돌려서 그룹 구분
    vector<pair<pair<int, int>, pair<int, int>>> groups = makeGroup();
    if (groups.size() == 0) {
      break;
    }

    // 가장 큰 그룹 찾기
    sort(groups.begin(), groups.end(), compare);
    pair<pair<int, int>, pair<int, int>> biggestGroup = groups[0];
    if (biggestGroup.second.first <= 1) {
      break;
    }

    // 가장 큰 그룹 제거 & 점수 추가
    score += removeGroup(biggestGroup.first);

    // 격자 중력
    applyGravity();

    // 반시계 90도 회전
    rotate();

    // 격자 중력
    applyGravity();
  }

  return score;
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
