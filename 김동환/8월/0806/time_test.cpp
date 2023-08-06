#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;


void vec_t(int size) {
  vector<int> arr;
  for(int i = 0; i < size; i++) {
    arr.push_back(i);
  }

  vector<int> tmp;
  for(int i = 0; i < size; i++) {
    tmp.push_back(arr[i]);
  }
}

void queue_t(int size) {
  queue<int> q;
  for(int i = 0; i < size; i++) {
    q.push(i);
  }

  queue<int> tmp;
  while(not q.empty()) {
    tmp.push(q.front());
    q.pop();
  }
}

void deque_t(int size) {
  deque<int> dq;
  for(int i = 0; i < size; i++) {
    dq.push_back(i);
  }

  deque<int> tmp;
  while(not dq.empty()) {
    tmp.push_back(dq.front());
    dq.pop_front();
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  for(int i = 10000000; i <= 50000000; i += 10000000) {
    cout << "size : " << i << endl;

    auto start = std::chrono::high_resolution_clock::now();
    vec_t(i);
    auto end = std::chrono::high_resolution_clock::now();
    chrono::microseconds elapsed = chrono::duration_cast<chrono::microseconds>(end - start);
    cout << "list time : " << elapsed.count() / 1000.0 << "ms\n";

    start = std::chrono::high_resolution_clock::now();
    queue_t(i);
    end = std::chrono::high_resolution_clock::now();
    elapsed = chrono::duration_cast<chrono::microseconds>(end - start);
    cout << "queue time : " << elapsed.count() / 1000.0 << "ms\n";

    start = std::chrono::high_resolution_clock::now();
    deque_t(i);
    end = std::chrono::high_resolution_clock::now();
    elapsed = chrono::duration_cast<chrono::microseconds>(end - start);
    cout << "deque time : " << elapsed.count() / 1000.0 << "ms\n\n";

  }

  return 0;
}
