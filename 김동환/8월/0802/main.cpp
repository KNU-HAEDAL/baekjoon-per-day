#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, start;
int graph[11][11];
bool visited[11];
int result = INF;

void dfs(int cur, int dist, int count) {
  if (result < dist) {
    return;
  }

  if (count == n) {
    result = min(result, dist);
    return;
  }

  for(int i = 0; i < n; i++) {
    if (not visited[i]) {
      visited[i] = true;
      dfs(i, dist + graph[cur][i], count + 1);
      visited[i] = false;
    }
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n >> start;

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      cin >> graph[i][j];
    }
  }

	for (int k = 0; k < n; k++)
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				if (graph[i][j] > graph[i][k] + graph[k][j])
					graph[i][j] = graph[i][k] + graph[k][j];

  visited[start] = true;
  dfs(start, 0, 1);

  cout << result << endl;

  return 0;
}
