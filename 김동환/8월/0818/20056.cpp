#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;

typedef tuple<int, int, int> Element;

int n, m, orderCount;
vector<vector<vector<Element>>> board;
int dy[] = {-1, -1, 0, 1, 1, 1, 0, -1}, dx[] = {0, 1, 1, 1, 0, -1, -1, -1};

int solve() {
  while(orderCount--) {
    vector<vector<vector<Element>>> tmp = vector<vector<vector<Element>>>(n, vector<vector<Element>>(n));

    // 이동
    for(int y = 0; y < n; y++) {
      for(int x = 0; x < n; x++) {
        for(Element ele : board[y][x]) {
          int weight, speed, dir;
          tie(weight, speed, dir) = ele;

          int ny = ((y + dy[dir] * speed) + n * speed) % n;
          int nx = ((x + dx[dir] * speed) + n * speed) % n;

          tmp[ny][nx].push_back({weight, speed, dir});
        }
      }
    }

    // 병합
    for(int y = 0; y < n; y++) {
      for(int x = 0; x < n; x++) {
        if (tmp[y][x].size() <= 1) {
          continue;
        }

        int weightSum = 0, speedSum = 0;
        bool isDirAllOddOrEven = true;
        for(int k = 0; k < tmp[y][x].size(); k++) {
          int weight, speed, dir;
          tie(weight, speed, dir) = tmp[y][x][k];;

          weightSum += weight;
          speedSum += speed;

          if (isDirAllOddOrEven and dir % 2 != get<2>(tmp[y][x][0]) % 2) {
            isDirAllOddOrEven = false;
          }
        }

        int weight = weightSum / 5;
        int speed = speedSum / tmp[y][x].size();
        tmp[y][x].clear();

        if (weight <= 0) {
          continue;
        }

        for(int i = 0; i < 4; i++) {
          int dir = isDirAllOddOrEven ? i * 2 : i * 2 + 1;

          tmp[y][x].push_back({weight, speed, dir});
        }
      }
    }

    board = tmp;
  }

  int result = 0;

  for(int y = 0; y < n; y++) {
    for(int x = 0; x < n; x++) {
      for(Element ele : board[y][x]) {
        result += get<0>(ele);
      }
    }
  }

  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n >> m >> orderCount;
  board = vector<vector<vector<Element>>>(n, vector<vector<Element>>(n));
  for(int i = 0; i < m; i++) {
    int y, x, weight, speed, dir;
    cin >> y >> x >> weight >> speed >> dir;

    board[y - 1][x - 1].push_back({weight, speed, dir});
  }

  cout << solve() << endl;

  return 0;
}
