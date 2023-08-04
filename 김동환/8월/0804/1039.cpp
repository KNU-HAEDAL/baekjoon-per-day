#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


string solve(string number, int k) {
  int m = number.size();

  if (m <= 1) {
    return "-1";
  }
  else if (m == 2 and number[1] == '0') {
    return "-1";
  }

  queue<string> q;
  q.push(number);
  int count = 0;
  string result = "0";

  while(not q.empty() and count < k) {
    int queueSize = q.size();
    set<string> visited;

    // 기존 큐에 들어있던 만큼 반복. count번 교환을 했을 때 만들어지는 모든 숫자에 대해 탐색 시작
    while(queueSize--) {
      string cur = q.front();
      q.pop();

      for(int i = 0; i < m - 1; i++) {
        for(int j = i + 1; j < m; j++) {
          if (i == 0 and cur[j] == '0') {
            continue;
          }

          swap(cur[i], cur[j]);
          if (visited.find(cur) == visited.end()) {
            if (count == k - 1 and result < cur) {
              result = cur;
            }

            q.push(cur);
            visited.insert(cur);
          }
          swap(cur[i], cur[j]);
        }
      }
    }

    count++;
  }

  // 만약 k번 스왑을 할 수 없는 경우, 즉 위 While문에서 q.empty()로 인해 탈출한 경우
  if (count != k) {
    return "-1";
  }

  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  string n;
  int k;
  cin >> n >> k;

  cout << solve(n, k) << endl;

  return 0;
}
