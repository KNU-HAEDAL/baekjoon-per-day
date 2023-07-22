#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


vector<int> graph[101];
bool visited[101];

int dfs(int start, int target, int count) {
  if (start == target) {
    return count;
  }

  int result = -1;
  visited[start] = true;
  for(int next : graph[start]) {
    if (not visited[next]) {
      result = dfs(next, target, count + 1);

      if (result != -1) {
        return result;
      }
    }
  }

  return -1;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  int n;
  cin >> n;

  int a, b;
  cin >> a >> b;

  int m;
  cin >> m;

  for(int i = 0; i < m; i++) {
    int x, y;
    cin >> x >> y;

    graph[x].push_back(y);
    graph[y].push_back(x);
  }

  cout << dfs(a, b, 0) << endl;

  return 0;
}
