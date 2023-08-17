#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	while(1) {
		int N, M;
		int count = 0;
		int ind_sang = 0, ind_sun = 0;
		long long tmp;
		vector<long long> sang;
		vector<long long> sun;

		cin >> N >> M;

		if (N == 0 && M == 0) break;

		for (int i = 0;i < N;i++) {
			cin >> tmp;
			sang.push_back(tmp);
		}

		for (int i = 0;i < M;i++) {
			cin >> tmp;
			sun.push_back(tmp);
		}
		
		while (1) {
			if (ind_sang==N || ind_sun==M)	break;
			if (sang[ind_sang] == sun[ind_sun]) {
				count++;
				ind_sang++;
				ind_sun++;
			}
			else if (sang[ind_sang] > sun[ind_sun])
				ind_sun++;
			else
				ind_sang++;
		}

		cout << count << "\n";
	}

	return 0;
}