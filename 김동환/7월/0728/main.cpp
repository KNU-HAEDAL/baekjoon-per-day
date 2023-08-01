#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


void solve11723() {
  int n;
  cin >> n;

  set<int> s;
  while(n--) {
    string operation;
    int operand;
    cin >> operation;

    if (operation == "add") {
      cin >> operand;
      s.insert(operand);
    }
    else if (operation == "remove") {
      cin >> operand;
      s.erase(operand);
    }
    else if (operation == "check") {
      cin >> operand;

      if (s.count(operand) == 1) {
        cout << "1\n";
      }
      else {
        cout << "0\n";
      }
    }
    else if (operation == "toggle") {
      cin >> operand;
      if (s.count(operand) == 1) {
        s.erase(operand);
      }
      else {
        s.insert(operand);
      }
    }
    else if (operation == "all") {
      for(int i = 1; i <= 20; i++) {
        s.insert(i);
      }
    }
    else {
      s.clear();
    }
  }
}

void solve10431() {
  int T;
  cin >> T;

  while(T--) {
    int t;
    cin >> t;

    int arr[20];
    for(int i = 0; i < 20; i++) {
      cin >> arr[i];
    }

    int count = 0;
    for(int i = 1; i < 20; i++) {
      for(int j = i - 1; j >= 0; j--) {
        if (arr[j + 1] < arr[j]) {
          int tmp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = tmp;
          count++;
        }
        else {
          break;
        }
      }
    }

    cout << t << " " << count << "\n";
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  solve11723();
  solve10431();

  return 0;
}
