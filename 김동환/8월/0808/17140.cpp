#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


int arr[101][101];

void sortRow(int rowSize, int &colSize) {
  for(int i = 0; i < rowSize; i++) {
    map<int, int> m;
    for(int j = 0; j < colSize; j++) {
      int val = arr[i][j];
      if (val == 0) {
        continue;
      }

      if (m.find(val) == m.end()) {
        m[val] = 1;
      }
      else {
        m[val] += 1;
      }
    }

    vector<pair<int, int>> tmp;
    for(pair<int, int> ele : m) {
      tmp.push_back({ele.second, ele.first});
    }

    sort(tmp.begin(), tmp.end());

    colSize = min(100, max(colSize, (int) tmp.size() * 2));
    for(int j = 0; j < tmp.size(); j++) {
      if (j * 2 >= 100) {
        break;
      }

      arr[i][j * 2] = tmp[j].second;
      arr[i][j * 2 + 1] = tmp[j].first;
    }
    for(int j = tmp.size() * 2; j < colSize; j++) {
      arr[i][j] = 0;
    }
  }
}

void sortCol(int &rowSize, int colSize) {
  for(int i = 0; i < colSize; i++) {
    map<int, int> m;
    for(int j = 0; j < rowSize; j++) {
      int val = arr[j][i];
      if (val == 0) {
        continue;;
      }

      if (m.find(val) == m.end()) {
        m[val] = 1;
      }
      else {
        m[val] += 1;
      }
    }

    vector<pair<int, int>> tmp;
    for(pair<int, int> ele : m) {
      tmp.push_back({ele.second, ele.first});
    }

    sort(tmp.begin(), tmp.end());

    rowSize = min(100, max(rowSize, (int) tmp.size() * 2));
    for(int j = 0; j < tmp.size(); j++) {
      if (j * 2 >= 100) {
        break;
      }

      arr[j * 2][i] = tmp[j].second;
      arr[j * 2 + 1][i] = tmp[j].first;
    }
    for(int j = tmp.size() * 2; j < rowSize; j++) {
      arr[j][i] = 0;
    }
  }
}

int solve(int r, int c, int k) {
  if (arr[r][c] == k) {
    return 0;
  }

  int result = 1, rowSize = 3, colSize = 3;
  for(; result <= 100; result++) {
    if (rowSize >= colSize) {
      sortRow(rowSize, colSize);
    }
    else {
      sortCol(rowSize, colSize);
    }

    if (arr[r][c] == k) {
      return result;
    }
  }

  return -1;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  int r, c, k;
  cin >> r >> c >> k;
  r--;
  c--;
  for(int i = 0; i < 3; i++) {
    for(int j = 0; j < 3; j++) {
      cin >> arr[i][j];
    }
  }

  cout << solve(r, c, k) << endl;

  return 0;
}
