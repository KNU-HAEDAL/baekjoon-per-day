#include <bits/stdc++.h>
#define INF 98765432
typedef long long ll;
using namespace std;


int n, e, u, v;
vector<pair<int, int>> graph[801];

int dijkstra(int start, int target) {
  priority_queue<pair<int, int>> pq;
  vector<int> dist(n + 1, INF);

  dist[start] = 0;
  pq.push({0, start});

  while(not pq.empty()) {
    int distance = -pq.top().first;
    int cur = pq.top().second;
    pq.pop();

    if (dist[cur] < distance) {
      continue;
    }

    for(int i = 0; i < graph[cur].size(); i++) {
      int next = graph[cur][i].first;
      int cost = graph[cur][i].second;
      int nextDistance = dist[cur] + cost;

      if (nextDistance < dist[next]) {
        dist[next] = nextDistance;
        pq.push({-nextDistance, next});
      }
    }
  }

  return dist[target];
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n >> e;

  for(int i = 0; i < e; i++) {
    int a, b, cost;
    cin >> a >> b >> cost;

    graph[a].push_back({b, cost});
    graph[b].push_back({a, cost});
  }

  cin >> u >> v;

  int s2u = dijkstra(1, u);
  int s2v = dijkstra(1, v);
  int u2v = dijkstra(u, v); // 단방향 그래프라서 하나만 구해도 됨
  int u2e = dijkstra(u, n);
  int v2e = dijkstra(v, n);

  // 경로가 아예 없을 경우 INF + INF + INF인데, INF가 987654321일 경우 int overflow 발생
  // 그래서 INF를 98765432로 설정함
  int result = min(s2u + u2v + v2e, s2v + u2v + u2e);

  cout << (result >= INF ? -1 : result) << endl;

  return 0;
}
