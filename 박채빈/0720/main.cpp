#include<iostream>
#include <utility>
#include <vector>

using namespace std;

vector<pair<int, int>> cnt;

void count_fibonacci(int N) {
	if (cnt.size() > N) return;
	else {
		for(int i=cnt.size();i <= N;i++)
			cnt.push_back({ cnt[i - 2].first + cnt[i - 1].first, cnt[i - 2].second + cnt[i - 1].second });
	}
}

int main(void) {
	int Test_case;
	int N;

	cnt.push_back( { 1, 0 });
	cnt.push_back({ 0, 1 });

	cin >> Test_case;

	for (int i = 0;i < Test_case;i++) {
		cin >> N;
		count_fibonacci(N);
		cout <<cnt[N].first << " " << cnt[N].second << endl;
	}


	return 0;
}