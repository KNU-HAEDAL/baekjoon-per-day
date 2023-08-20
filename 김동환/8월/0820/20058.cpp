#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, q;
int board[65][65];
int dy[] = {-1, 0, 1, 0}, dx[] = {0, 1, 0, -1};

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < n;
}

void rotate(int startY, int startX, int l) {
  int tmp[65][65] = {0};

  int endY = startY + l, endX = startX + l;
  for(int i = startY; i < endY; i++) {
    for(int j = startX; j < endX; j++) {
      tmp[j - startX + startY][endY - i - 1 + startX] = board[i][j];
    }
  }

  for(int i = startY; i < endY; i++) {
    for(int j = startX; j < endX; j++) {
      board[i][j] = tmp[i][j];
    }
  }
}

void decreaseIce() {
  int tmp[65][65] = {0};

  for(int y = 0; y < n; y++) {
    for(int x = 0; x < n; x++) {
      if (board[y][x] <= 0) {
        continue;
      }

      int adjacentIceCount = 0;
      for(int dir = 0; dir < 4; dir++) {
        int ny = y + dy[dir];
        int nx = x + dx[dir];

        if (isInside(ny, nx) and board[ny][nx] > 0) {
          adjacentIceCount++;
        }
      }

      if (adjacentIceCount >= 3) {
        tmp[y][x] = board[y][x];
      }
      else {
        tmp[y][x] = board[y][x] - 1;
      }
    }
  }

  for(int y = 0; y < n; y++) {
    for(int x = 0; x < n; x++) {
      board[y][x] = tmp[y][x];
    }
  }
}

int bfs(int sy, int sx, bool visited[][65]) {
  queue<pair<int, int>> q;

  int visitedCount = 1;
  q.push({sy, sx});
  visited[sy][sx] = true;
  while(not q.empty()) {
    int y = q.front().first;
    int x = q.front().second;
    q.pop();

    for(int i = 0; i < 4; i++) {
      int ny = y + dy[i];
      int nx = x + dx[i];

      if (isInside(ny, nx) and not visited[ny][nx] and board[ny][nx] > 0) {
        q.push({ny, nx});
        visited[ny][nx] = true;
        visitedCount++;
      }
    }
  }

  return visitedCount;
}

void solve() {
  while(q--) {
    int l;
    cin >> l;
    l = pow(2, l);

    for(int i = 0; i < n; i += l) {
      for(int j = 0; j < n; j += l) {
        rotate(i, j, l);
      }
    }

    decreaseIce();
  }

  bool visited[65][65] = {false};
  int sumOfIce = 0, maxSizeOfIce = 0;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      sumOfIce += board[i][j];

      if (not visited[i][j] and board[i][j] > 0) {
        maxSizeOfIce = max(maxSizeOfIce, bfs(i, j, visited));
      }
    }
  }

  cout << sumOfIce << endl << maxSizeOfIce << endl;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n >> q;
  n = pow(2, n);
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      cin >> board[i][j];
    }
  }

  solve();

  return 0;
}
