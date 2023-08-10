#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n;
int board[21][21];

int getResult(int x, int y, int d1, int d2) {
  int area[21][21] = {0};

  // (x, y), (x+1, y-1), ..., (x+d1, y-d1)
  int r = x, c = y;
  while(r <= x + d1 and c >= y - d1) {
    area[r][c] = 5;

    r++;
    c--;
  }
  if (r <= x + d1 or c >= y - d1) {
    return INF;
  }

  // (x, y), (x+1, y+1), ..., (x+d2, y+d2)
  r = x; c = y;
  while(r <= x + d2 and c <= y + d2) {
    area[r][c] = 5;

    r++;
    c++;
  }
  if (r <= x + d2 or c <= y + d2) {
    return INF;
  }

  // (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
  r = x + d1; c = y - d1;
  while(r <= x + d1 + d2 and c <= y - d1 + d2) {
    area[r][c] = 5;

    r++;
    c++;
  }
  if (r <= x + d1 + d2 or c <= y - d1 + d2) {
    return INF;
  }

  // (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
  r = x + d2; c = y + d2;
  while(r <= x + d1 + d2 and c >= y - d1 + d2) {
    area[r][c] = 5;

    r++;
    c--;
  }
  if (r <= x + d1 + d2 or c >= y - d1 + d2) {
    return INF;
  }

  for(int i = 1; i <= n; i++) {
    bool isInside5 = false;
    for(int j = 1; j <= n; j++) {
      if (area[i][j] == 5) {
        if (i != x and i != x + d1 + d2) {
          isInside5 = not isInside5;
        }

        continue;
      }
      else if (isInside5) {
        area[i][j] = 5;
        continue;
      }

      /*
      1번 선거구: 1 ≤ i < x + d1, 1 ≤ j ≤ y
      2번 선거구: 1 ≤ i ≤ x + d2, y < j ≤ N
      3번 선거구: x + d1 ≤ i ≤ N, 1 ≤ j < y - d1 + d2
      4번 선거구: x + d2 < i ≤ N, y - d1 + d2 ≤ j ≤ N
      */
      if (i < x + d1 and j <= y) {
        area[i][j] = 1;
      }
      else if (i <= x + d2 and y < j) {
        area[i][j] = 2;
      }
      else if (x + d1 <= i and j < y - d1 + d2) {
        area[i][j] = 3;
      }
      else {
        area[i][j] = 4;
      }
    }
  }

  int population[5] = {0};
  for(int i = 1; i <= n; i++) {
    for(int j = 1; j <= n; j++) {
      int curArea = area[i][j] - 1;
      int curPopulation = board[i][j];

      population[curArea] += curPopulation;
    }
  }

  sort(population, population + 5);

  return population[4] - population[0];
}

int solve() {
  int result = INF;

  // (d1, d2 ≥ 1, 1 ≤ x < x + d1 + d2 ≤ N, 1 ≤ y - d1 < y < y + d2 ≤ N)
  for(int x = 1; x <= n; x++) {
    for(int y = 1; y <= n; y++) {
      for(int d1 = 1; 1 <= y - d1; d1++) {
        for(int d2 = 1; y + d2 <= n and x + d1 + d2 <= n; d2++) {
          result = min(result, getResult(x, y, d1, d2));
        }
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
  for(int i = 1; i <= n; i++) {
    for(int j = 1; j <= n; j++) {
      cin >> board[i][j];
    }
  }

  cout << solve() << endl;

  return 0;
}
