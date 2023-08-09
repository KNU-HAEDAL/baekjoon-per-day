#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, m;
int board[51][51];
vector<pair<int, int>> viruses;
int dy[] = {-1, 0, 1, 0}, dx[] = {0, 1, 0, -1};

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < n;
}

int solve() {
  int result = INF;

  int countEmpty = 0;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      if (board[i][j] == 0) {
        countEmpty++;
      }
    }
  }

  vector<int> comb(viruses.size() - m, 0);
  for(int i = 0; i < m; i++) {
    comb.push_back(1);
  }

  do {
    queue<pair<pair<int, int>, int>> q;
    bool visited[51][51] = {false};

    for(int i = 0; i < viruses.size(); i++) {
      if (comb[i] == 1) {
        q.push({viruses[i], 0});
        visited[viruses[i].first][viruses[i].second] = true;
      }
    }

    int maxDist = 0, tCountEmpty = countEmpty;
    while(not q.empty()) {
      int y = q.front().first.first;
      int x = q.front().first.second;
      int dist = q.front().second;
      q.pop();

      for(int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (isInside(ny, nx) and not visited[ny][nx] and board[ny][nx] != 1) {
          q.push({{ny, nx}, dist + 1});
          visited[ny][nx] = true;

          if (board[ny][nx] == 0) {
            tCountEmpty--;

            if (tCountEmpty == 0) {
              maxDist = dist + 1;
              break;
            }
          }
        }
      }
    }

    if (tCountEmpty == 0) {
      result = min(result, maxDist);
    }
  } while(next_permutation(comb.begin(), comb.end()));

  if (result == INF) {
    return -1;
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

      if (board[i][j] == 2) {
        viruses.push_back({i, j});
      }
    }
  }

  cout << solve() << endl;

  return 0;
}
