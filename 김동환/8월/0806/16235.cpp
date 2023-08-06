#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, m, targetYear;
int droneMineral[11][11], dieMineral[11][11], mineral[11][11];
int dy[] = {-1, -1, 0, 1, 1, 1, 0, -1}, dx[] = {0, 1, 1, 1, 0, -1, -1, -1};
vector<int> trees[11][11];

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < n;
}

void springAndFall() {
  queue<pair<int, int>> newTrees;

  for(int y = 0; y < n; y++) {
    for(int x = 0; x < n; x++) {
      sort(trees[y][x].begin(), trees[y][x].end());

      vector<int> tmp;
      for(int k = 0; k < trees[y][x].size(); k++) {
        int year = trees[y][x][k];

        if (year <= mineral[y][x]) {
          mineral[y][x] -= year;
          tmp.push_back(year + 1);

          if ((year + 1) % 5 == 0) {
            for(int i = 0; i < 8; i++) {
              int ny = y + dy[i];
              int nx = x + dx[i];

              if (isInside(ny, nx)) {
                newTrees.push({ny, nx});
              }
            }
          }
        }
        else {
          dieMineral[y][x] += year / 2;
        }
      }
      trees[y][x] = tmp;
    }
  }

  while(not newTrees.empty()) {
    int y = newTrees.front().first;
    int x = newTrees.front().second;
    newTrees.pop();

    trees[y][x].push_back(1);
  }
}

void summerAndWinter() {
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      mineral[i][j] += droneMineral[i][j] + dieMineral[i][j];
      dieMineral[i][j] = 0;
    }
  }
}

int solve() {
  while(targetYear--) {
    springAndFall();
    summerAndWinter();
  }

  int result = 0;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      result += trees[i][j].size();
    }
  }

  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n >> m >> targetYear;

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      mineral[i][j] = 5;
      cin >> droneMineral[i][j];
    }
  }

  for(int i = 0; i < m; i++) {
    int y, x, year;
    cin >> y >> x >> year;

    trees[y - 1][x - 1].push_back(year);
  }

  cout << solve() << endl;

  return 0;
}
