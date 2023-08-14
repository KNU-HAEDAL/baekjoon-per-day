#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, m, fuel, startY, startX;
vector<int> board[21][21];
int dy[] = {-1, 0, 1, 0}, dx[] = {0, 1, 0, -1};

struct compare {
  bool operator()(pair<pair<int, int>, int> a, pair<pair<int, int>, int> b) {
    if (a.second != b.second) {
      return a.second > b.second;
    }
    if (a.first.first != b.first.first) {
      return a.first.first > b.first.first;
    }
    return a.first.second > b.first.second;
  }
};

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < n;
}

int solve() {
  while(m--) {
    // 태울 손님 찾기
    priority_queue<pair<pair<int, int>, int>, vector<pair<pair<int, int>, int>>, compare> pq;
    bool visited[21][21] = { false };

    pq.push({{startY, startX}, 0});
    visited[startY][startX] = true;

    int customer = -1, distToCustomer = 0;
    while(not pq.empty()) {
      int y = pq.top().first.first;
      int x = pq.top().first.second;
      int dist = pq.top().second;
      pq.pop();

      if (board[y][x].size() > 1) {
        for(int i = 1; i < board[y][x].size(); i++) {
          if (board[y][x][i] > 1) {
            customer = board[y][x][i];
            board[y][x].erase(board[y][x].begin() + i);
            break;
          }
        }

        if (customer != -1) {
          distToCustomer = dist;
          startY = y;
          startX = x;
          break;
        }
      }

      for(int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (isInside(ny, nx) and not visited[ny][nx] and board[ny][nx][0] == 0) {
          pq.push({{ny, nx}, dist + 1});
          visited[ny][nx] = true;
        }
      }
    }

    // 태울 손님에게로 도달할 수 없다면 종료
    if (customer == -1) {
      return -1;
    }

    // 태울 손님까지 가는 연료 계산
    if (fuel < distToCustomer) {
      return -1;
    }
    fuel -= distToCustomer;

    // 손님의 목적지까지 가기
    queue<pair<pair<int, int>, int>> q;
    memset(visited, false, sizeof(visited));

    q.push({{startY, startX}, 0});
    visited[startY][startX] = true;

    int distToDest = -1;
    while(not q.empty()) {
      int y = q.front().first.first;
      int x = q.front().first.second;
      int dist = q.front().second;
      q.pop();

      if (board[y][x].size() > 1) {
        for(int i = 1; i < board[y][x].size(); i++) {
          if (board[y][x][i] == -customer) {
            distToDest = dist;
            board[y][x].erase(board[y][x].begin() + i);
            break;
          }
        }

        if (distToDest != -1) {
          startY = y;
          startX = x;
          break;
        }
      }

      for(int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (isInside(ny, nx) and not visited[ny][nx] and board[ny][nx][0] == 0) {
          q.push({{ny, nx}, dist + 1});
          visited[ny][nx] = true;
        }
      }
    }

    // 목적지까지 도달할 수 없으면 종료
    if (distToDest == -1) {
      return -1;
    }

    // 목적지까지 가는 연료 계산
    if (fuel < distToDest) {
      return -1;
    }

    fuel += distToDest;
  }

  return fuel;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n >> m >> fuel;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      int ele;
      cin >> ele;
      board[i][j].push_back(ele);
    }
  }

  cin >> startY >> startX;
  startY--;
  startX--;

  for(int i = 2; i <= m + 1; i++) {
    int sy, sx, ey, ex;
    cin >> sy >> sx >> ey >> ex;

    board[sy - 1][sx - 1].push_back(i);
    board[ey - 1][ex - 1].push_back(-i);
  }

  cout << solve() << endl;

  return 0;
}