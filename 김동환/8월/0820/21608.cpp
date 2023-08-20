#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n;
int board[21][21];
int priorities[401][4];
int dy[] = {-1, 0, 1, 0}, dx[] = {0, 1, 0, -1};

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < n;
}

bool compare(pair<pair<int, int>, pair<int, int>> a, pair<pair<int, int>, pair<int, int>> b) {
  if (a.second.first != b.second.first) {
    return a.second.first > b.second.first;
  }
  if (a.second.second != b.second.second) {
    return a.second.second > b.second.second;
  }
  if (a.first.first != b.first.first) {
    return a.first.first < b.first.first;
  }
  return a.first.second < b.first.second;
}

int solve() {
  for(int t1 = 0; t1 < n * n; t1++) {
    int studentId;
    cin >> studentId;

    for(int i = 0; i < 4; i++) {
      cin >> priorities[studentId][i];
    }

    map<pair<int, int>, int> adjacentPriorCounts;
    map<pair<int, int>, int> adjacentEmptyCounts;
    for(int y = 0; y < n; y++) {
      for(int x = 0; x < n; x++) {
        if (board[y][x] > 0) {
          continue;
        }

        adjacentEmptyCounts[{y, x}] = 0;
        adjacentPriorCounts[{y, x}] = 0;

        for(int dir = 0; dir < 4; dir++) {
          int ny = y + dy[dir];
          int nx = x + dx[dir];

          if (isInside(ny, nx)) {
            if (board[ny][nx] == 0) {
              adjacentEmptyCounts[{y, x}]++;
            }
            else {
              for(int i = 0; i < 4; i++) {
                int priorStudent = priorities[studentId][i];

                if (board[ny][nx] == priorStudent) {
                  adjacentPriorCounts[{y, x}]++;
                  break;
                }
              }
            }
          }
        }
      }
    }

    vector<pair<pair<int, int>, pair<int, int>>> arr;
    for(int y = 0; y < n; y++) {
      for(int x = 0; x < n; x++) {
        if (board[y][x] > 0) {
          continue;
        }

        int emptyCount = adjacentEmptyCounts[{y, x}];
        int priorCount = adjacentPriorCounts[{y, x}];
        arr.push_back({{y, x}, {priorCount, emptyCount}});
      }
    }

    sort(arr.begin(), arr.end(), compare);

    int y = arr[0].first.first;
    int x = arr[0].first.second;

    board[y][x] = studentId;
  }

  int result = 0;
  for(int y = 0; y < n; y++) {
    for(int x = 0; x < n; x++) {
      int priorCount = 0, studentId = board[y][x];

      for(int dir = 0; dir < 4; dir++) {
        int ny = y + dy[dir];
        int nx = x + dx[dir];

        if (isInside(ny, nx)) {
          for(int i = 0; i < 4; i++) {
            if (board[ny][nx] == priorities[studentId][i]) {
              priorCount++;
              break;
            }
          }
        }
      }

      if (priorCount == 1) {
        result++;
      }
      else if (priorCount == 2) {
        result += 10;
      }
      else if (priorCount == 3) {
        result += 100;
      }
      else if (priorCount == 4) {
        result += 1000;
      }
    }
  }

  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n;

  cout << solve() << endl;

  return 0;
}
