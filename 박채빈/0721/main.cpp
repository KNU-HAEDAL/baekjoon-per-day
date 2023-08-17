#include <iostream>	
#include <vector>

using namespace std;

int main(void) {
	int N;
	int turn;
	vector<int> order;

	cin >> N;

	for (int i = 0;i < N;i++) {
		cin >> turn;
		order.insert(order.begin() + (i - turn), i);
	}

	for (int i = 0;i < N;i++) {
		cout << order[i]+1<<" ";
	}

	return 0;
}