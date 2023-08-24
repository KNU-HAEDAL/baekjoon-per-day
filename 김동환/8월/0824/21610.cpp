#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, m;
int board[51][51];
int dy[] = {0, -1, -1, -1, 0, 1, 1, 1}, dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < n;
}

int solve() {
  vector<pair<int, int>> clouds;

  clouds.push_back({n - 1, 0});
  clouds.push_back({n - 1, 1});
  clouds.push_back({n - 2, 0});
  clouds.push_back({n - 2, 1});

  while(m--) {
    int dir, speed;
    cin >> dir >> speed;
    dir--;

    // 구름 이동
    int cloudCount = clouds.size();
    for(int i = 0; i < cloudCount; i++) {
      int y = clouds[i].first;
      int x = clouds[i].second;

      int ny = ((y + dy[dir] * speed) + n * speed) % n;
      int nx = ((x + dx[dir] * speed) + n * speed) % n;

      clouds.push_back({ny, nx});
    }
    clouds.erase(clouds.begin(), clouds.begin() + cloudCount);

    // 비 내리기
    set<pair<int, int>> increasedCells;
    for(auto cloud : clouds) {
      int y = cloud.first;
      int x = cloud.second;

      board[y][x]++;
      increasedCells.insert({y, x});
    }

    // 구름 제거
    clouds.clear();

    // 물 복사 버그
    map<pair<int, int>, int> increaseWater;
    for(auto cell : increasedCells) {
      int y = cell.first;
      int x = cell.second;

      increaseWater[{y, x}] = 0;
      for(int i = 1; i < 8; i += 2) {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (isInside(ny, nx) and board[ny][nx] > 0) {
          increaseWater[{y, x}]++;
        }
      }
    }

    for(auto ele : increaseWater) {
      int y = ele.first.first;
      int x = ele.first.second;
      int amount = ele.second;

      board[y][x] += amount;
    }

    // 구름 생성
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n; j++) {
        if (board[i][j] >= 2 and increasedCells.find({i, j}) == increasedCells.end()) {
          clouds.push_back({i, j});
          board[i][j] -= 2;
        }
      }
    }
  }

  int result = 0;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      result += board[i][j];
    }
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
