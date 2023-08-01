#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, target, start, u, d;
bool visited[1000001];

int bfs() {
  queue<pair<int, int>> q;

  q.push({start, 0});
  visited[start] = true;

  while(not q.empty()) {
    int cur = q.front().first;
    int count = q.front().second;
    q.pop();

    if (cur == target) {
      return count;
    }

    if (cur + u <= n and not visited[cur + u]) {
      q.push({cur + u, count + 1});
      visited[cur + u] = true;
    }

    if (cur - d >= 1 and not visited[cur - d]) {
      q.push({cur - d, count + 1});
      visited[cur - d] = true;
    }
  }

  return -1;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n >> start >> target >> u >> d;

  int result = bfs();

  if (result == -1) {
    cout << "use the stairs\n";
  }
  else {
    cout << result << endl;
  }

  return 0;
}
