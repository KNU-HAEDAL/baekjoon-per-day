#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, m, k;
pair<int, int> board[21][21];
pair<pair<int, int>, int> shark[401];
int priorities[401][4][4];
int dy[] = {-1, 1, 0, 0}, dx[] = {0, 0, -1, 1};

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < n;
}

int solve() {
  for(int time = 1; time <= 1000; time++) {
    // 이동
    for(int i = 1; i <= m; i++) {
      int y = shark[i].first.first;
      int x = shark[i].first.second;
      int dir = shark[i].second;

      if (y == -1) {
        continue;
      }

      // 주변이 모두 다른 상어의 냄새일 가능성은 없다. 즉, 빈 칸이 있는 경우 or 빈 칸이 없는 경우(자신의 냄새가 하나 이상 있음)
      bool existsEmptyCell = false;
      for(int j = 0; j < 4; j++) {
        int ndir = priorities[i][dir][j];
        int ny = y + dy[ndir];
        int nx = x + dx[ndir];

        if (isInside(ny, nx) and board[ny][nx].first == 0) {
          existsEmptyCell = true;

          shark[i].first = make_pair(ny, nx);
          shark[i].second = ndir;

          break;
        }
      }

      if (not existsEmptyCell) {
        for(int j = 0; j < 4; j++) {
          int ndir = priorities[i][dir][j];
          int ny = y + dy[ndir];
          int nx = x + dx[ndir];

          if (isInside(ny, nx) and board[ny][nx].first == i) {
            shark[i].first = make_pair(ny, nx);
            shark[i].second = ndir;

            break;
          }
        }
      }
    }

    // 기존 냄새 카운트 감소 및 제거
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n; j++) {
        board[i][j].second--;
        if (board[i][j].second <= 0) {
          board[i][j].first = 0;
        }
      }
    }

    // 쫒아내기
    set<pair<int, int>> s;
    for(int i = 1; i <= m; i++) {
      if (s.find(shark[i].first) == s.end()) {
        s.insert(shark[i].first);
      }
      else {
        shark[i] = make_pair(make_pair(-1, -1), -1);
      }
    }

    // 냄새 뿌리기
    for(int i = 1; i <= m; i++) {
      int y = shark[i].first.first;
      int x = shark[i].first.second;

      if (y != -1) {
        board[y][x] = make_pair(i, k);
      }
    }

    // 검증
    bool existsOtherShark = false;
    for(int i = 2; i <= m; i++) {
      if (shark[i].first.first != -1) {
        existsOtherShark = true;
        break;
      }
    }

    if (not existsOtherShark) {
      return time;
    }
  }

  return -1;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n >> m >> k;

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      int ele;
      cin >> ele;

      if (ele > 0) {
        shark[ele].first = make_pair(i, j);
        board[i][j] = make_pair(ele, k);
      }
    }
  }

  for(int i = 1; i <= m; i++) {
    cin >> shark[i].second;

    shark[i].second--;
  }

  for(int i = 1; i <= m; i++) {
    for(int j = 0; j < 4; j++) {
      for(int k = 0; k < 4; k++) {
        cin >> priorities[i][j][k];
        priorities[i][j][k]--;
      }
    }
  }

  cout << solve() << endl;

  return 0;
}