#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, m, t, start, g, h;
vector<pair<int, int>> graph[2001];

void dijkstra(vector<int> &dist, int start) {
  priority_queue<pair<int, int>> pq;

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
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  int T;
  cin >> T;

  while(T--) {
    for(int i = 0; i <= 2000; i++) {
      graph[i].clear();
    }

    cin >> n >> m >> t >> start >> g >> h;

    for(int i = 0; i < m; i++) {
      int a, b, cost;
      cin >> a >> b >> cost;

      graph[a].push_back({b, cost});
      graph[b].push_back({a, cost});
    }

    vector<int> distS(n + 1, INF);
    vector<int> distG(n + 1, INF);
    vector<int> distH(n + 1, INF);
    dijkstra(distS, start);
    dijkstra(distG, g);
    dijkstra(distH, h);
    int costG2H = distG[h];

    vector<int> result;
    for(int i = 0; i < t; i++) {
      int x;
      cin >> x;

      if (distS[x] == distS[g] + costG2H + distH[x]) {
        result.push_back(x);
      }
      else if (distS[x] == distS[h] + costG2H + distG[x]) {
        result.push_back(x);
      }
    }

    sort(result.begin(), result.end());

    for(int ele : result) {
      cout << ele << " ";
    }
    cout << endl;
  }

  return 0;
}
