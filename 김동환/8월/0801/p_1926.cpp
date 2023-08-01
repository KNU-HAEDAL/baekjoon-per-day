#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, m;
int board[501][501];
bool visited[501][501];
int dy[] = {-1, 0, 1, 0}, dx[] = {0, 1, 0, -1};

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < m;
}

int bfs(int startY, int startX) {
  queue<pair<int, int>> q;

  q.push({startY, startX});
  visited[startY][startX] = true;

  int result = 0;
  while(!q.empty()) {
    int y = q.front().first;
    int x = q.front().second;
    q.pop();

    result++;

    for(int i = 0; i < 4; i++) {
      int ny = y + dy[i];
      int nx = x + dx[i];

      if (isInside(ny, nx) and not visited[ny][nx] and board[ny][nx] == 1) {
        q.push({ny, nx});
        visited[ny][nx] = true;
      }
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
    for(int j = 0; j < m; j++) {
      cin >> board[i][j];
    }
  }

  int result = 0, count = 0;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      if (not visited[i][j] and board[i][j] == 1) {
        result = max(result, bfs(i, j));
        count++;
      }
    }
  }

  cout << count << endl << result << endl;

  return 0;
}
