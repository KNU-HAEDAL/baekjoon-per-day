#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;

#define UP 1
#define DOWN 2
#define RIGHT 3
#define LEFT 4


int n, m, sharkCount;
tuple<int, int, int> board[101][101];

int getFish(int x) {
  for(int i = 0; i < n; i++) {
    int fishSize = get<2>(board[i][x]);

    if (fishSize > 0) {
      board[i][x] = make_tuple(0, 0, 0);
      return fishSize;
    }
  }

  return 0;
}

void moveFish() {
  // vector<vector<vector<tuple<int, int, int>>>> tmp(n, vector<vector<tuple<int, int, int>>>(m, vector<tuple<int, int, int>>()));
  vector<tuple<int, int, int>> tmp[101][101];

  for(int y = 0; y < n; y++) {
    for(int x = 0; x < m; x++) {
      int speed, dir, size;
      tie(speed, dir, size) = board[y][x];

      if (size == 0) {
        continue;
      }

      int ny = y, nx = x, remainSpeed = speed, nDir = dir;
      if (dir == UP) {
        if (y <= remainSpeed) {
          // 가장 위쪽으로 이동
          remainSpeed -= y;
          ny = 0;
          nDir = DOWN;

          // 왔다갔다 제거
          remainSpeed = remainSpeed % ((n - 1) * 2);

          if (remainSpeed >= (n - 1)) {
            // 반대편 끝까지 갈 수 있으면 감
            remainSpeed -= n - 1;
            ny = n - 1;
            nDir = UP;

            // 남은 거리 이동
            if (remainSpeed > 0) {
              ny -= remainSpeed;
              remainSpeed = 0;
            }
          }
          else {
            // 아래쪽 끝까지 못가면, 남은 속도만큼 아래로 이동한다.
            ny = remainSpeed;
            remainSpeed = 0;
          }
        }
        else {
          // 반대편 끝까지 못가는 경우, 그냥 위쪽으로 조금 이동한다.
          ny -= remainSpeed;
          remainSpeed = 0;
        }
      }
      else if (dir == DOWN) {
        if (n - y - 1 <= remainSpeed) {
          // 가장 아래쪽으로 이동
          remainSpeed -= n - y - 1;
          ny = n - 1;
          nDir = UP;

          // 왔다갔다 제거
          remainSpeed = remainSpeed % ((n - 1) * 2);

          if (remainSpeed >= (n - 1)) {
            // 위쪽 끝까지 갈 수 있으면 감
            remainSpeed -= n - 1;
            ny = 0;
            nDir = DOWN;

            // 남은 거리 이동
            if (remainSpeed > 0) {
              ny = remainSpeed;
              remainSpeed = 0;
            }
          }
          else {
            // 위쪽 끝까지 못가면, 남은 속도만큼 위로 이동한다.
            ny -= remainSpeed;
            remainSpeed = 0;
          }
        }
        else {
          // 반대편 끝까지 못가는 경우, 그냥 아래쪽으로 조금 이동한다.
          ny += remainSpeed;
          remainSpeed = 0;
        }
      }
      else if (dir == RIGHT) {
        if (m - x - 1 <= remainSpeed) {
          // 가장 오른쪽으로 이동
          remainSpeed -= m - x - 1;
          nx = m - 1;
          nDir = LEFT;


          // 왔다갔다 제거
          remainSpeed = remainSpeed % ((m - 1) * 2);

          if (remainSpeed >= (m - 1)) {
            // 왼쪽 끝까지 갈 수 있으면 감
            remainSpeed -= m - 1;
            nx = 0;
            nDir = RIGHT;

            // 남은 거리 이동
            if (remainSpeed > 0) {
              nx = remainSpeed;
              remainSpeed = 0;
            }
          }
          else {
            // 왼쪽 끝까지 못가면, 남은 속도만큼 왼쪽으로 이동한다.
            nx -= remainSpeed;
            remainSpeed = 0;
          }
        }
        else {
          // 반대편 끝까지 못가는 경우, 그냥 오른쪽으로 조금 이동한다.
          nx += remainSpeed;
          remainSpeed = 0;
        }
      }
      else {
        if (x <= remainSpeed) {
          // 가장 왼쪽으로 이동
          remainSpeed -= x;
          nx = 0;
          nDir = RIGHT;

          // 왔다갔다 제거
          remainSpeed = remainSpeed % ((m - 1) * 2);

          if (remainSpeed >= (m - 1)) {
            // 오른쪽 끝까지 갈 수 있으면 감
            remainSpeed -= m - 1;
            nx = m - 1;
            nDir = LEFT;

            // 남은 거리 이동
            if (remainSpeed > 0) {
              nx -= remainSpeed;
              remainSpeed = 0;
            }
          }
          else {
            // 오른쪽 끝까지 못가면, 남은 속도만큼 오른쪽으로 이동한다.
            nx = remainSpeed;
            remainSpeed = 0;
          }
        }
        else {
          // 반대편 끝까지 못가는 경우, 그냥 왼쪽으로 조금 이동한다.
          nx -= remainSpeed;
          remainSpeed = 0;
        }
      }

      board[y][x] = make_tuple(0, 0, 0);
      tmp[ny][nx].push_back({speed, nDir, size});
    }
  }

  for(int y = 0; y < n; y++) {
    for(int x = 0; x < m; x++) {
      if (tmp[y][x].size() == 0) {
        continue;
      }

      int mSpeed, mDir, maxSize = -1;
      for(int i = 0; i < tmp[y][x].size(); i++) {
        int speed, dir, size;
        tie(speed, dir, size) = tmp[y][x][i];

        if (maxSize < size) {
          maxSize = size;
          mSpeed = speed;
          mDir = dir;
        }
      }

      board[y][x] = make_tuple(mSpeed, mDir, maxSize);
    }
  }
}

int solve() {
  int result = 0;
  for(int fisherX = 0; fisherX < m; fisherX++) {
    result += getFish(fisherX);

    moveFish();
  }

  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n >> m >> sharkCount;

  for(int i = 0; i < sharkCount; i++) {
    int y, x, speed, dir, size;

    cin >> y >> x >> speed >> dir >> size;

    board[y - 1][x - 1] = make_tuple(speed, dir, size);
  }

  cout << solve() << endl;

  return 0;
}
