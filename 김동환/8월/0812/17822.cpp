#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, m, t;
deque<int> board[51];

void rotate(int x, int d, int k) {
  for(int i = x; i <= n; i += x) {
    for(int j = 0; j < k; j++) {
      if (d == 0) {
        board[i].push_front(board[i].back());
        board[i].pop_back();
      }
      else {
        board[i].push_back(board[i].front());
        board[i].pop_front();
      }
    }
  }
}

void postProcess() {
  int sum = 0, eleCount = 0;
  set<pair<int, int>> adjacentSamePoses;
  for(int i = 1; i <= n; i++) {
    for(int j = 0; j < m; j++) {
      if (board[i][j] == -1) {
        continue;
      }

      sum += board[i][j];
      eleCount++;

      int leftX = (j + m - 1) % m;
      int rightX = (j + 1) % m;
      int upY = i - 1;
      int downY = i + 1;

      if (board[i][j] == board[i][leftX]) {
        adjacentSamePoses.insert({i, j});
        adjacentSamePoses.insert({i, leftX});
      }
      if (board[i][j] == board[i][rightX]) {
        adjacentSamePoses.insert({i, j});
        adjacentSamePoses.insert({i, rightX});
      }
      if (upY > 0 and board[i][j] == board[upY][j]) {
        adjacentSamePoses.insert({i, j});
        adjacentSamePoses.insert({upY, j});
      }
      if (downY <= n and board[i][j] == board[downY][j]) {
        adjacentSamePoses.insert({i, j});
        adjacentSamePoses.insert({downY, j});
      }
    }
  }

  if (adjacentSamePoses.size() == 0) {
    double average = (double) sum / eleCount;

    for(int i = 1; i <= n; i++) {
      for(int j = 0; j < m; j++) {
        if (board[i][j] == -1) {
          continue;
        }
        else if (board[i][j] > average) {
          board[i][j]--;
        }
        else if (board[i][j] < average) {
          board[i][j]++;
        }
      }
    }

    return;
  }

  for(pair<int, int> ele : adjacentSamePoses) {
    int y = ele.first;
    int x = ele.second;

    board[y][x] = -1;
  }
}

int solve() {
  while(t--) {
    int x, d, k;
    cin >> x >> d >> k;

    rotate(x, d, k);
    postProcess();
  }

  int sum = 0;
  for(int i = 1; i <= n; i++) {
    for(int j = 0; j < m; j++) {
      if (board[i][j] != -1) {
        sum += board[i][j];
      }
    }
  }

  return sum;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n >> m >> t;
  for(int i = 1; i <= n; i++) {
    for(int j = 0; j < m; j++) {
      int tmp;
      cin >> tmp;

      board[i].push_back(tmp);
    }
  }

  cout << solve() << endl;

  return 0;
}