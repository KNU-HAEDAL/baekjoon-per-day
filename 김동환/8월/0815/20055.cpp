#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int n, k;
deque<int> belt;
deque<int> robots;

int solve() {
  int phase = 0;

  while(true) {
    phase++;

    // 벨트 회전
    belt.push_front(belt.back());
    belt.pop_back();

    for(int i = 0; i < robots.size(); i++) {
      robots[i]++;
    }
    if (not robots.empty() and robots.front() == n - 1) {
      robots.pop_front();
    }

    // 로봇 이동
    for(int i = 0; i < robots.size(); i++) {
      int curPos = robots[i];
      int nextPos = curPos + 1;

      if (belt[nextPos] > 0 and (i == 0 or robots[i - 1] != nextPos)) {
        robots[i] = nextPos;
        belt[nextPos]--;
      }
    }
    if (not robots.empty() and robots.front() == n - 1) {
      robots.pop_front();
    }

    // 로봇 올리기
    if (belt[0] > 0) {
      robots.push_back(0);
      belt[0]--;
    }

    // 칸 검증 (성능 개선할려면, 내구도가 0이 된 칸을 set으로 관리하면 될 듯)
    int count = 0;
    for(int i = 0; i < 2 * n; i++) {
      if (belt[i] == 0) {
        count++;
      }
    }

    if (count >= k) {
      break;
    }
  }

  return phase;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n >> k;
  for(int i = 0; i < 2 * n; i++) {
    int ele;
    cin >> ele;

    belt.push_back(ele);
  }

  cout << solve() << endl;

  return 0;
}