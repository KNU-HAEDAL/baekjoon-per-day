#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


bool isPossible = false;

void solve(string s, string t) {
  if (isPossible) {
    return;
  }

  if (s.size() == t.size()) {
    if (s == t) {
      isPossible = true;
    }

    return;
  }

  if (t[t.size() - 1] == 'A') {
    string temp = t;
    temp.erase(temp.size() - 1);

    solve(s, temp);
  }

  if (t[0] == 'B') {
    string temp = t;
    temp.erase(temp.begin());
    reverse(temp.begin(), temp.end());

    solve(s, temp);
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  string s, t;
  cin >> s >> t;

  solve(s, t);

  cout << (isPossible ? 1 : 0) << endl;

  return 0;
}
