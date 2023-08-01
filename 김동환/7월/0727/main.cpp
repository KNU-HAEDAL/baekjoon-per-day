#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int solve(string a, string b) {
  int n = a.size(), m = b.size();

  vector<vector<int>> dp(n, vector<int>(m, 0));

  int result = 0;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      if (a[i] == b[j]) {
        if (i > 0 and j > 0) {
          dp[i][j] = dp[i - 1][j - 1] + 1;
          result = max(result, dp[i][j]);
        }
        else {
          dp[i][j] = 1;
          result = max(result, dp[i][j]);
        }
      }
    }
  }

  return result;
}


int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  string a, b;
  cin >> a >> b;

  cout << solve(a, b) << endl;

  return 0;
}
