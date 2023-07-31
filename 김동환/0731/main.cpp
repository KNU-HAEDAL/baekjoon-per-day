#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  int n, s, r;
  cin >> n >> s >> r;

  vector<int> arr(n + 1, 0);

  for(int i = 0; i < s; i++) {
    int pos;
    cin >> pos;

    arr[pos] = 1;
  }

  for(int i = 0; i < r; i++) {
    int pos;
    cin >> pos;

    if (arr[pos] == 1) {
      arr[pos] = 0;
    }
    else {
      arr[pos] = 2;
    }
  }

  int count = 0;
  for(int i = 1; i <= n; i++) {
    if (arr[i] == 1) {
      if (arr[i - 1] == 2) {
        arr[i - 1] = 0;
        arr[i] = 0;
      }
      else if (arr[i + 1] == 2) {
        arr[i + 1] = 0;
        arr[i] = 0;
      }
      else {
        count++;
      }
    }
  }

  cout << count << endl;

  return 0;
}
