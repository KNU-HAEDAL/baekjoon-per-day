#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, m;
string board[1001];
bool visited[1001][1001];
int dy[] = {-1, 0, 1, 0}, dx[] = {0, 1, 0, -1};

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < m;
}

bool isEscape(int y, int x) {
  return y == 0 or y == n - 1 or x == 0 or x == m - 1;
}

int solve() {
  // y, x, dist, isFire
  queue<tuple<int, int, int, bool>> q;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      if (board[i][j] == 'F') {
        q.push({i, j, 0, true});
        visited[i][j] = true;
      }
    }
  }
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      if (board[i][j] == 'J') {
        q.push({i, j, 0, false});
        visited[i][j] = true;
        break;
      }
    }
  }

  while(!q.empty()) {
    int y, x, dist;
    bool isFire;
    tie(y, x, dist, isFire) = q.front();
    q.pop();

    if (not isFire and isEscape(y, x)) {
      return dist + 1;
    }

    for(int i = 0; i < 4; i++) {
      int ny = y + dy[i];
      int nx = x + dx[i];

      if (isInside(ny, nx) and not visited[ny][nx] and board[ny][nx] != '#') {
        q.push({ny, nx, dist + 1, isFire});
        visited[ny][nx] = true;
      }
    }
  }

  return -1;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n >> m;

  for(int i = 0; i < n; i++) {
    cin >> board[i];
  }

  int result = solve();

  if (result == -1) {
    cout << "IMPOSSIBLE\n";
  }
  else {
    cout << result << endl;
  }

  return 0;
}
