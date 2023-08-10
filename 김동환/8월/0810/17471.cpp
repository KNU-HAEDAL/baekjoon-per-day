#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n;
int populations[10];
vector<int> graph[10];

int bfs(vector<bool> &area, bool type) {
  bool visited[10] = { false };
  queue<int> q;
  for(int i = 0; i < n; i++) {
    if (area[i] == type) {
      q.push(i);
      visited[i] = true;
      break;
    }
  }

  int count = 1;
  while(not q.empty()) {
    int cur = q.front();
    q.pop();

    for(int next : graph[cur]) {
      if (not visited[next] and area[next] == type) {
        q.push(next);
        visited[next] = true;
        count++;
      }
    }
  }

  return count;
}

int solve() {
  int result = INF;

  for(int aCount = 1; aCount < n; aCount++) {
    vector<bool> comb(aCount, false);
    for(int i = aCount; i < n; i++) {
      comb.push_back(true);
    }

    do {
      int bfsACount = bfs(comb, false);
      int bfsBCount = bfs(comb, true);

      if (bfsACount + bfsBCount < n) {
        continue;
      }

      int aPopulation = 0, bPopulation = 0;
      for(int i = 0; i < n; i++) {
        if (comb[i]) {
          bPopulation += populations[i];
        }
        else {
          aPopulation += populations[i];
        }
      }

      result = min(result, abs(aPopulation - bPopulation));
    }while(next_permutation(comb.begin(), comb.end()));
  }

  if (result == INF) {
    return -1;
  }

  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n;
  for(int i = 0; i < n; i++) {
    cin >> populations[i];
  }

  for(int i = 0; i < n; i++) {
    int edgeCount = 0;
    cin >> edgeCount;

    while(edgeCount--) {
      int other;
      cin >> other;

      graph[i].push_back(other - 1);
    }
  }

  cout << solve() << endl;

  return 0;
}
