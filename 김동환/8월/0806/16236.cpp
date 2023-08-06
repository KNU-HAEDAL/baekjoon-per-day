#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n;
int board[21][21];
int dy[] = {-1, 0, 0, 1}, dx[] = {0, -1, 1, 0};

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < n;
}

struct compare {
  bool operator()(pair<pair<int, int>, int> a, pair<pair<int, int>, int> b) {
    if (a.second != b.second) {
      return a.second > b.second;
    }
    if (a.first.first != b.first.first) {
      return a.first.first > b.first.first;
    }
    return a.first.second > b.first.second;
  }
};

int solve() {
  int totalElapsedTime = 0, sharkSize = 2, upgradeCount = 0;
  int startY, startX;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      if (board[i][j] == 9) {
        startY = i;
        startX = j;
        board[i][j] = 0;
        break;
      }
    }
  }

  while(true) {
    bool visited[21][21] = {false};
    priority_queue<
      pair<pair<int, int>, int>,
      vector<pair<pair<int, int>, int>>,
      compare
    > pq;

    pq.push({{startY, startX}, totalElapsedTime});
    visited[startY][startX] = true;

    bool isEaten = false;
    while(not pq.empty()) {
      int y = pq.top().first.first;
      int x = pq.top().first.second;
      int elapsedTime = pq.top().second;
      pq.pop();

      if (0 < board[y][x] and board[y][x] < sharkSize) {
        isEaten = true;
        totalElapsedTime = elapsedTime;
        board[y][x] = 0;
        startY = y;
        startX = x;
        break;
      }

      for(int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (isInside(ny, nx) and not visited[ny][nx] and board[ny][nx] <= sharkSize) {
          pq.push({{ny, nx}, elapsedTime + 1});
          visited[ny][nx] = true;
        }
      }
    }

    if (isEaten) {
      upgradeCount++;
      if (upgradeCount == sharkSize) {
        sharkSize++;
        upgradeCount = 0;
      }
    }
    else {
      break;
    }
  }

  return totalElapsedTime;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n;

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      cin >> board[i][j];
    }
  }

  cout << solve() << endl;

  return 0;
}
