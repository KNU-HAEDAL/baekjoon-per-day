#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, m;
string board[101];
int visited[101][101][4];
int dy[] = {-1, 0, 1, 0}, dx[] = {0, 1, 0, -1};

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < m;
}

int solve() {
  int sy = -1, sx = -1, ey, ex;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      for(int k = 0; k < 4; k++) {
        visited[i][j][k] = INF;
      }
      if (board[i][j] == 'C') {
        if (sy == -1) {
          sy = i;
          sx = j;
        }
        else {
          ey = i;
          ex = j;
        }
      }
    }
  }

  // mirrorCount, y, x, dir
  priority_queue<tuple<int, int, int, int>> pq;

  for(int i = 0; i < 4; i++) {
    pq.push({0, sy, sx, i});
    visited[sy][sx][i] = INF;
  }

  while(!pq.empty()) {
    int mirrorCount, y, x, dir;
    tie(mirrorCount, y, x, dir) = pq.top();
    mirrorCount *= -1;
    pq.pop();

    if (y == ey and x == ex) {
      return mirrorCount;
    }

    int ny, nx, nDir;

    for(int i = -1; i <= 1; i++) {
      int nDir = (dir + 4 + i) % 4;
      int ny = y + dy[nDir];
      int nx = x + dx[nDir];
      int nMirrorCount = mirrorCount + (dir == nDir ? 0 : 1);

      if (isInside(ny, nx) and visited[ny][nx][nDir] > nMirrorCount and board[ny][nx] != '*') {
        pq.push({-nMirrorCount, ny, nx, nDir});
        visited[ny][nx][nDir] = nMirrorCount;
      }
    }
  }

  return -1;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> m >> n;
  for(int i = 0; i < n; i++) {
    cin >> board[i];
  }

  cout << solve() << endl;

  return 0;
}
