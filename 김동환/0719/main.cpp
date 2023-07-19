#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  int n, x;
  cin >> n;

  vector<int> arr(n);
  for(int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  cin >> x;

  sort(arr.begin(), arr.end());

  int result = 0;
  int i = 0, j = n - 1;
  while(i < j) {
    if (arr[i] + arr[j] == x) {
      result++;
      i++;
      j--;
    }
    else if (arr[i] + arr[j] < x) {
      i++;
    }
    else {
      j--;
    }
  }

  cout << result << endl;

  return 0;
}
