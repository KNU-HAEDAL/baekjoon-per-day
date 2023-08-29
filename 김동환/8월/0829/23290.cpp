#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int magicCount;
int dy[] = {0, -1, -1, -1, 0, 1, 1, 1}, dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
vector<vector<vector<int>>> fishes, smells;
int sharkY, sharkX;


bool isInside(int y, int x) {
  return 0 <= y and y < 4 and 0 <= x and x < 4;
}

bool existsShark(int y, int x) {
  return sharkY == y and sharkX == x;
}

bool existsSmell(int y, int x) {
  return smells[y][x].size() > 0;
}

pair<pair<int, int>, int> findNextPos(int y, int x, int dir) {
  int resultY = y, resultX = x, resultDir = dir;

  for(int j = 0; j < 8; j++) {
    int ndir = (dir + 8 - j) % 8;
    int ny = y + dy[ndir];
    int nx = x + dx[ndir];

    if (isInside(ny, nx) and not existsShark(ny, nx) and not existsSmell(ny, nx)) {
      resultY = ny;
      resultX = nx;
      resultDir = ndir;
      break;
    }
  }

  return make_pair(make_pair(resultY, resultX), resultDir);
}

void moveFishes() {
  vector<vector<vector<int>>> tmp = vector<vector<vector<int>>>(4, vector<vector<int>>(4));

  for(int y = 0; y < 4; y++) {
    for(int x = 0; x < 4; x++) {
      for(int dir : fishes[y][x]) {
        pair<pair<int, int>, int> nextPos = findNextPos(y, x, dir);
        int ny = nextPos.first.first;
        int nx = nextPos.first.second;
        int ndir = nextPos.second;

        tmp[ny][nx].push_back(ndir);
      }
    }
  }

  fishes = tmp;
}

int getFishCount(int y, int x) {
  return fishes[y][x].size();
}

void moveShark() {
  vector<pair<int, int>> routes;

  int sharkDy[] = {-1, 0, 1, 0}, sharkDx[] = {0, -1, 0, 1};
  for(int i = 0; i < 4; i++) {
    int firstMovedY = sharkY + sharkDy[i];
    int firstMovedX = sharkX + sharkDx[i];
    if (not isInside(firstMovedY, firstMovedX)) {
      continue;
    }

    int firstFishCount = getFishCount(firstMovedY, firstMovedX);

    for(int j = 0; j < 4; j++) {
      int secondMovedY = firstMovedY + sharkDy[j];
      int secondMovedX = firstMovedX + sharkDx[j];
      if (not isInside(secondMovedY, secondMovedX)) {
        continue;
      }

      int secondFishCount = getFishCount(secondMovedY, secondMovedX);

      for(int k = 0; k < 4; k++) {
        int thirdMovedY = secondMovedY + sharkDy[k];
        int thirdMovedX = secondMovedX + sharkDx[k];
        if (not isInside(thirdMovedY, thirdMovedX)) {
          continue;
        }

        int thirdFishCount = getFishCount(thirdMovedY, thirdMovedX);
        // 세번째 이동의 경우, 첫번째 이동한 곳으로 돌아갈 수도 있음
        if (firstMovedY == thirdMovedY and firstMovedX == thirdMovedX) {
          thirdFishCount = 0;
        }

        int fishCount = firstFishCount + secondFishCount + thirdFishCount;
        int dirPriority = i * 100 + j * 10 + k;

        routes.push_back({-fishCount, dirPriority});
      }
    }
  }

  sort(routes.begin(), routes.end());
  int route = routes.front().second;

  for(int i = 100; i > 0; i /= 10) {
    int curDir = (route % (i * 10)) / i;

    sharkY = sharkY + sharkDy[curDir];
    sharkX = sharkX + sharkDx[curDir];

    if (fishes[sharkY][sharkX].size() > 0) {
      fishes[sharkY][sharkX].clear();
      smells[sharkY][sharkX].push_back(2);
    }
  }
}

void updateSmell() {
  for(int y = 0; y < 4; y++) {
    for(int x = 0; x < 4; x++) {
      int n = smells[y][x].size();

      for(int i = 0; i < n; i++) {
        if (smells[y][x][i] > 0) {
          smells[y][x].push_back(smells[y][x][i] - 1);
        }
      }

      smells[y][x].erase(smells[y][x].begin(), smells[y][x].begin() + n);
    }
  }
}

int solve() {
  while(magicCount--) {
    // 복제 마법 시전
    vector<vector<vector<int>>> copiedFishes = fishes;

    // 물고기 이동
    moveFishes();

    // 상어 이동
    moveShark();

    // 오래된 냄새 제거
    updateSmell();

    // 복제 마법 적용
    for(int y = 0; y < 4; y++) {
      for(int x = 0; x < 4; x++) {
        for(int copiedFishDir : copiedFishes[y][x]) {
          fishes[y][x].push_back(copiedFishDir);
        }
      }
    }
  }

  int count = 0;

  for(int y = 0; y < 4; y++) {
    for(int x = 0; x < 4; x++) {
      count += fishes[y][x].size();
    }
  }

  return count;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  fishes = vector<vector<vector<int>>>(4, vector<vector<int>>(4));
  smells = vector<vector<vector<int>>>(4, vector<vector<int>>(4));

  int m;
  cin >> m >> magicCount;

  for(int i = 0; i < m; i++) {
    int y, x, dir;
    cin >> y >> x >> dir;

    fishes[y - 1][x - 1].push_back(dir - 1);
  }

  cin >> sharkY >> sharkX;
  sharkY--; sharkX--;

  cout << solve() << endl;

  return 0;
}
