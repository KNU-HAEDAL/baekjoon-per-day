#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


void solve25966() {
  int n, m, q;
  cin >> n >> m >> q;

  vector<vector<int>> arr(n, vector<int>(m));
  vector<int> mapper(n);
  for(int i = 0; i < n; i++) {
    mapper[i] = i;
    for(int j = 0; j < m; j++) {
      cin >> arr[i][j];
    }
  }

  while(q--) {
    int oper, i, j;
    cin >> oper >> i >> j;

    if (oper == 0) {
      int k;
      cin >> k;

      int row = mapper[i];
      arr[row][j] = k;
    }
    else {
      int tmp = mapper[i];
      mapper[i] = mapper[j];
      mapper[j] = tmp;
    }
  }

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      cout << arr[mapper[i]][j] << " ";
    }
    cout << "\n";
  }
}

void solve25972() {
  int n;
  cin >> n;

  vector<pair<int, int>> arr(n);
  for(int i = 0; i < n; i++) {
    cin >> arr[i].first >> arr[i].second;
  }

  sort(arr.begin(), arr.end());

  int result = 0, prevX = -1;
  for(int i = 0; i < n; i++) {
    if (arr[i].first > prevX) {
      result++;
    }

    prevX = arr[i].first + arr[i].second;
  }

  cout << result << endl;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  solve25966();
  solve25972();

  return 0;
}
