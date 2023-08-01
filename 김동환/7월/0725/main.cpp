#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  int n, l;
  cin >> n >> l;

  vector<pair<int, int>> arr;
  for(int i = 0; i < n; i++) {
    int s, e;
    cin >> s >> e;

    arr.push_back({s, e});
  }

  sort(arr.begin(), arr.end());

  int result = 0;
  int prevPlankEnd = -1;
  for(pair<int, int> ele : arr) {
    int holeStart = ele.first;
    int holeEnd = ele.second;

    int plankStart = holeStart;
    if (plankStart < prevPlankEnd) {
      plankStart = prevPlankEnd;
    }
    int holeLength = holeEnd - plankStart;
    int plankCount = ceil((double)holeLength / l);

    result += plankCount;
    prevPlankEnd = plankStart + plankCount * l;
  }

  cout << result << endl;

  return 0;
}
