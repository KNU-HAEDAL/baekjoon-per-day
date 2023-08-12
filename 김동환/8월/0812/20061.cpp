#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;

int n;
vector<bool> blueBoard[7], greenBoard[7];
int score = 0;

void putBlock(int y, int x, int type) {
  if (type == 1) {
    // 1x1 Block을 (y, x)에 둠
    for(int i = 0; i < 6; i++) {
      if (not blueBoard[i][y] and blueBoard[i + 1][y]) {
        blueBoard[i][y] = true;
        break;
      }
    }

    for(int i = 0; i < 6; i++) {
      if (not greenBoard[i][x] and greenBoard[i + 1][x]) {
        greenBoard[i][x] = true;
        break;
      }
    }
  }
  else if (type == 2) {
    // 1x2 Block을 (y, x), (y, x + 1)에 둠.
    for(int i = 1; i < 6; i++) {
      if (not blueBoard[i][y] and blueBoard[i + 1][y]) {
        blueBoard[i - 1][y] = true;
        blueBoard[i][y] = true;
        break;
      }
    }

    for(int i = 0; i < 6; i++) {
      if (not greenBoard[i][x] and not greenBoard[i][x + 1] and (greenBoard[i + 1][x] or greenBoard[i + 1][x + 1])) {
        greenBoard[i][x] = true;
        greenBoard[i][x + 1] = true;
        break;
      }
    }
  }
  else {
    // 2x1 Block을 (y, x), (y + 1, x)에 둠.
    for(int i = 0; i < 6; i++) {
      if (not blueBoard[i][y] and not blueBoard[i][y + 1] and (blueBoard[i + 1][y] or blueBoard[i + 1][y + 1])) {
        blueBoard[i][y] = true;
        blueBoard[i][y + 1] = true;
        break;
      }
    }

    for(int i = 1; i < 6; i++) {
      if (not greenBoard[i][x] and greenBoard[i + 1][x]) {
        greenBoard[i - 1][x] = true;
        greenBoard[i][x] = true;
        break;
      }
    }
  }
}

void removeFilledLine() {
  for(int i = 5; i >= 0; i--) {
    bool isFilled = true;
    for(int j = 0; j < 4; j++) {
      if (not blueBoard[i][j]) {
        isFilled = false;
        break;
      }
    }

    if (isFilled) {
      score++;

      for(int j = i; j > 0; j--) {
        blueBoard[j] = blueBoard[j - 1];
      }
      blueBoard[0] = vector<bool>(4, false);
      i++;
    }
  }

  for(int i = 5; i >= 0; i--) {
    bool isFilled = true;
    for(int j = 0; j < 4; j++) {
      if (not greenBoard[i][j]) {
        isFilled = false;
        break;
      }
    }

    if (isFilled) {
      score++;

      for(int j = i; j > 0; j--) {
        greenBoard[j] = greenBoard[j - 1];
      }
      greenBoard[0] = vector<bool>(4, false);
      i++;
    }
  }
}

void removeSpecialLine() {
  for(int i = 0; i < 2; i++) {
    bool existsBlock = false;
    for(int j = 0; j < 4; j++) {
      if (blueBoard[1][j]) {
        existsBlock = true;
        break;
      }
    }

    if (existsBlock) {
      for(int j = 5; j > 0; j--) {
        blueBoard[j] = blueBoard[j - 1];
      }
      blueBoard[0] = vector<bool>(4, false);
    }
  }

  for(int i = 0; i < 2; i++) {
    bool existsBlock = false;
    for(int j = 0; j < 4; j++) {
      if (greenBoard[1][j]) {
        existsBlock = true;
        break;
      }
    }

    if (existsBlock) {
      for(int j = 5; j > 0; j--) {
        greenBoard[j] = greenBoard[j - 1];
      }
      greenBoard[0] = vector<bool>(4, false);
    }
  }
}

void solve() {
  for(int i = 0; i < 6; i++) {
    blueBoard[i] = vector<bool>(4, false);
    greenBoard[i] = vector<bool>(4, false);
  }
  blueBoard[6] = vector<bool>(4, true);
  greenBoard[6] = vector<bool>(4, true);

  while(n--) {
    int type, y, x;
    cin >> type >> y >> x;

    putBlock(y, x, type);
    removeFilledLine();
    removeSpecialLine();
  }

  int tileCount = 0;

  for(int i = 0; i < 6; i++) {
    for(int j = 0; j < 4; j++) {
      if (blueBoard[i][j]) {
        tileCount++;
      }
      if (greenBoard[i][j]) {
        tileCount++;
      }
    }
  }

  cout << score << endl;
  cout << tileCount << endl;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n;

  solve();

  return 0;
}
