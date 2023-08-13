#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;

#define SHARK -1
#define EMPTY 0


pair<pair<int, int>, int> fishes[17];
int board[4][4];
int dy[] = {-1, -1, 0, 1, 1, 1, 0, -1}, dx[] = {0, -1, -1, -1, 0, 1, 1, 1};
int result = 0;

void setFishes(int id, int y, int x, int dir) {
  fishes[id] = make_pair(make_pair(y, x), dir);
}

bool isInside(int y, int x) {
  return 0 <= y and y < 4 and 0 <= x and x < 4;
}

void moveFish(int sharkY, int sharkX) {
  for(int id = 1; id <= 16; id++) {
    if (fishes[id].second == -1) {
      continue;
    }

    int fishY = fishes[id].first.first;
    int fishX = fishes[id].first.second;
    int fishDir = fishes[id].second;

    // 이동할 수 없는 경우가 존재하지 않음.
    while(true) {
      int ny = fishY + dy[fishDir];
      int nx = fishX + dx[fishDir];

      if (isInside(ny, nx) and not (ny == sharkY and nx == sharkX)) {
        if (board[ny][nx] == EMPTY) {
          setFishes(id, ny, nx, fishDir);

          board[ny][nx] = id;
          board[fishY][fishX] = EMPTY;
        }
        else {
          int otherId = board[ny][nx];

          setFishes(id, ny, nx, fishDir);
          setFishes(otherId, fishY, fishX, fishes[otherId].second);

          board[ny][nx] = id;
          board[fishY][fishX] = otherId;
        }

        break;
      }

      fishDir = (fishDir + 1) % 8;
    }
  }
}

void dfs(int sharkY, int sharkX, int sharkDir, int sumId) {
  result = max(result, sumId);

  // 기존 배열 복사
  int tmpBoard[4][4];
  for(int i = 0; i < 4; i++) {
    for(int j = 0; j < 4; j++) {
      tmpBoard[i][j] = board[i][j];
    }
  }
  pair<pair<int, int>, int> tmpFishes[17];
  for(int id = 1; id <= 16; id++) {
    tmpFishes[id] = fishes[id];
  }

  moveFish(sharkY, sharkX);

  while(isInside(sharkY, sharkX)) {
    if (board[sharkY][sharkX] != EMPTY) {
      int fishId = board[sharkY][sharkX];
      int fishDir = fishes[fishId].second;

      setFishes(fishId, -1, -1, -1);
      board[sharkY][sharkX] = EMPTY;

      dfs(sharkY, sharkX, fishDir, sumId + fishId);

      board[sharkY][sharkX] = fishId;
      setFishes(fishId, sharkY, sharkX, fishDir);
    }

    sharkY = sharkY + dy[sharkDir];
    sharkX = sharkX + dx[sharkDir];
  }

  // 기존 배열 복구
  for(int i = 0; i < 4; i++) {
    for(int j = 0; j < 4; j++) {
      board[i][j] = tmpBoard[i][j];
    }
  }
  for(int i = 1; i <= 16; i++) {
    fishes[i] = tmpFishes[i];
  }
}


int solve() {
  int startY = 0, startX = 0;
  int startId = board[startY][startX];
  int dir = fishes[startId].second;

  board[startY][startX] = EMPTY;
  setFishes(startId, -1, -1, -1);

  dfs(startY, startX, dir, startId);

  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  for(int i = 0; i < 4; i++) {
    for(int j = 0; j < 4; j++) {
      int id, dir;
      cin >> id >> dir;

      fishes[id] = make_pair(make_pair(i, j), dir - 1);
      board[i][j] = id;
    }
  }

  cout << solve() << endl;

  return 0;
}