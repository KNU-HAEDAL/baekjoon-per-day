#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  int n, k;
  cin >> n >> k;

  vector<int> arr(n);
  for(int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  sort(arr.begin(), arr.end());

  vector<int> diff;
  for(int i = 1; i < n; i++) {
    diff.push_back(arr[i] - arr[i - 1]);
  }

  sort(diff.begin(), diff.end());

  int result = 0;
  for(int i = 0; i < n - 1 - (k - 1); i++) {
    result += diff[i];
  }

  cout << result << endl;

  return 0;
}
