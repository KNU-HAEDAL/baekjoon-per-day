#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, m, k;
int board[201][201], visited[201][201][31];
vector<pair<int, int>> pattern;

int dy[] = {-1, 0, 1, 0};
int dx[] = {0, 1, 0, -1};

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < m;
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

  for(int i = -2; i <=2; i++) {
    for(int j = -2; j <= 2; j++) {
      int tmp;
      cin >> tmp;

      if (tmp == 1) {
        pattern.push_back({i, j});
      }
    }
  }

  int result = -1;
  // y, x, usePatternCount, dist, passedMid
  queue<tuple<int, int, int, int, bool>> q;
  q.push({0, 0, 0, 0, false});
  visited[0][0][0] = 1;
  while(!q.empty()) {
    int y, x, count, dist, passedMid;
    tie(y, x, count, dist, passedMid) = q.front();
    q.pop();

    if (y == n - 1 and x == m - 1 and passedMid) {
      result = dist;
      break;
    }

    for(int i = 0; i < 4; i++) {
      int ny = y + dy[i];
      int nx = x + dx[i];

      if (isInside(ny, nx)) {
        if (not passedMid and visited[ny][nx][count] == 0) {
          if (board[ny][nx] == 0) {
            q.push({ny, nx, count, dist + 1, false});
            visited[ny][nx][count] = 1;
          }
          else if (board[ny][nx] == 2) {
            q.push({ny, nx, count, dist + 1, true});
            visited[ny][nx][count] = 2;
          }
        }
        else if (passedMid and visited[ny][nx][count] <= 1) {
          if (board[ny][nx] != 1) {
            q.push({ny, nx, count, dist + 1, true});
            visited[ny][nx][count] = 2;
          }
        }
      }
    }

    if (count < k) {
      for(pair<int, int> pos : pattern) {
        int ny = y + pos.first;
        int nx = x + pos.second;

        if (isInside(ny, nx)) {
          if (not passedMid and visited[ny][nx][count + 1] == 0) {
            if (board[ny][nx] == 0) {
              q.push({ny, nx, count + 1, dist + 1, false});
              visited[ny][nx][count + 1] = 1;
            }
            else if (board[ny][nx] == 2) {
              q.push({ny, nx, count + 1, dist + 1, true});
              visited[ny][nx][count + 1] = 2;
            }
          }
          else if (passedMid and visited[ny][nx][count + 1] <= 1) {
            if (board[ny][nx] != 1) {
              q.push({ny, nx, count + 1, dist + 1, true});
              visited[ny][nx][count + 1] = 2;
            }
          }
        }
      }
    }
  }

  cout << result << endl;

  return 0;
}
