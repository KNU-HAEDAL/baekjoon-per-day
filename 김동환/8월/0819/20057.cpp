#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n;
int board[500][500];
int dy[] = {0, 1, 0, -1}, dx[] = {-1, 0, 1, 0};
double tornado[4][5][5] = {
  {
    {0, 0, 0.02, 0, 0},
    {0, 0.1, 0.07, 0.01, 0},
    {0.05, 0, 0, 0, 0},
    {0, 0.1, 0.07, 0.01, 0},
    {0, 0, 0.02, 0, 0}
  },
  {
    {0, 0, 0, 0, 0},
    {0, 0.01, 0, 0.01, 0},
    {0.02, 0.07, 0, 0.07, 0.02},
    {0, 0.1, 0, 0.1, 0},
    {0, 0, 0.05, 0, 0}
  },
  {
    {0, 0, 0.02, 0, 0},
    {0, 0.01, 0.07, 0.1, 0},
    {0, 0, 0, 0, 0.05},
    {0, 0.01, 0.07, 0.1, 0},
    {0, 0, 0.02, 0, 0}
  },
  {
    {0, 0, 0.05, 0, 0},
    {0, 0.1, 0, 0.1, 0},
    {0.02, 0.07, 0, 0.07, 0.02},
    {0, 0.01, 0, 0.01, 0},
    {0, 0, 0, 0, 0}
  }
};

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < n;
}

int solve() {
  int distPerLine = 1, y = n / 2, x = n / 2, dir = 0;
  int movedOutsideSand = 0;

  while(true) {
    for(int t1 = 0; t1 < 2; t1++) {
      for(int t2 = 0; t2 < distPerLine; t2++) {
        y = y + dy[dir];
        x = x + dx[dir];

        if (x == -1) {
          return movedOutsideSand;
        }

        int sumMovedSand = 0;
        for(int i = 0; i < 5; i++) {
          for(int j = 0; j < 5; j++) {
            int movedSand = board[y][x] * tornado[dir][i][j];
            sumMovedSand += movedSand;

            int ty = y + i - 2;
            int tx = x + j - 2;
            if (isInside(ty, tx)) {
              board[ty][tx] += movedSand;
            }
            else {
              movedOutsideSand += movedSand;
            }
          }
        }

        int remainSand = board[y][x] - sumMovedSand;
        board[y][x] = 0;

        if (isInside(y + dy[dir], x + dx[dir])) {
          board[y + dy[dir]][x + dx[dir]] += remainSand;
        }
        else {
          movedOutsideSand += remainSand;
        }
      }

      dir = (dir + 1) % 4;
    }

    distPerLine++;
  }

  return -1;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      cin >> board[i][j];
    }
  }

  cout << solve() << endl;

  return 0;
}
